"""Flask APP to manage the GeoServer."""
import argparse
import logging
import os
import pathlib
import re
import sqlite3
import uuid

import retrying


DATABASE_PATH = 'manager.db'

logging.basicConfig(
    level=logging.DEBUG,
    format=(
        '%(asctime)s (%(relativeCreated)d) %(processName)s %(levelname)s '
        '%(name)s [%(funcName)s:%(lineno)d] %(message)s'))
LOGGER = logging.getLogger(__name__)


@retrying.retry(wait_exponential_multiplier=1000, wait_exponential_max=5000)
def _execute_sqlite(
        sqlite_command, database_path, argument_list=None,
        mode='read_only', execute='execute', fetch=None):
    """Execute SQLite command and attempt retries on a failure.

    Parameters:
        sqlite_command (str): a well formatted SQLite command.
        database_path (str): path to the SQLite database to operate on.
        argument_list (list): `execute == 'execute` then this list is passed to
            the internal sqlite3 `execute` call.
        mode (str): must be either 'read_only' or 'modify'.
        execute (str): must be either 'execute', 'many', or 'script'.
        fetch (str): if not `None` can be either 'all' or 'one'.
            If not None the result of a fetch will be returned by this
            function.

    Returns:
        result of fetch if `fetch` is not None.

    """
    cursor = None
    connection = None
    try:
        if mode == 'read_only':
            ro_uri = r'%s?mode=ro' % pathlib.Path(
                os.path.abspath(database_path)).as_uri()
            LOGGER.debug(
                '%s exists: %s', ro_uri, os.path.exists(os.path.abspath(
                    database_path)))
            connection = sqlite3.connect(ro_uri, uri=True)
        elif mode == 'modify':
            connection = sqlite3.connect(database_path)
        else:
            raise ValueError('Unknown mode: %s' % mode)

        if execute == 'execute':
            cursor = connection.execute(sqlite_command, argument_list)
        elif execute == 'many':
            cursor = connection.executemany(sqlite_command, argument_list)
        elif execute == 'script':
            cursor = connection.executescript(sqlite_command)
        else:
            raise ValueError('Unknown execute mode: %s' % execute)

        result = None
        payload = None
        if fetch == 'all':
            payload = (cursor.fetchall())
        elif fetch == 'one':
            payload = (cursor.fetchone())
        elif fetch is not None:
            raise ValueError('Unknown fetch mode: %s' % fetch)
        if payload is not None:
            result = list(payload)
        cursor.close()
        connection.commit()
        connection.close()
        return result
    except Exception:
        LOGGER.exception('Exception on _execute_sqlite: %s', sqlite_command)
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.commit()
            connection.close()
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GeoServer API key manager')
    parser.add_argument(
        '--api_key', type=str, help='base api_key, required unless --create')
    parser.add_argument(
        '--create', action='store_true',
        help='create a new api key, will print to stdout')
    parser.add_argument(
        '--add_permission', type=str, default=[], nargs='+', help=(
            'list of permissions to add ex.: WRITE:myworkspace '
            'READ:*'))
    parser.add_argument(
        '--delete', action='store_true', help='delete the api key')
    args = parser.parse_args()

    # XOR api_key or create
    if bool(args.api_key) != args.create:
        raise ValueError('only --api_key or --create must be set.')

    if args.create and args.delete:
        raise ValueError('cannot delete and create')

    for permission in args.add_permission:
        if not re.match(r"^(READ:|WRITE:)([a-z0-9]+|\*)$", permission):
            raise ValueError(f'invalid permission: "{permission}"')

    if args.create:
        api_key = uuid.uuid4().hex
    else:
        api_key = args.api_key

    if args.create:
        _execute_sqlite(
            '''
            INSERT INTO api_keys (key, permissions)
            VALUES (?, ?)
            ''', DATABASE_PATH, argument_list=[
                api_key, ' '.join(args.add_permission)],
            mode='modify', execute='execute')
    elif args.add_permission:
        # get old permissions to add onto
        original_permissions = _execute_sqlite(
            '''
            SELECT permissions
            FROM api_keys
            WHERE api_key=?
            ''', DATABASE_PATH, mode='read_only', execute='execute',
            argument_list=[api_key], fetch='one')
        if original_permissions is None:
            raise ValueError(f'{api_key} not valid')
        new_permissions = ' '.join(
            set(original_permissions[0].split(' ')) + set(args.add_permission))
        _execute_sqlite(
            '''
            UPDATE api_keys
            SET permissions=?
            WHERE api_key=?
            ''', DATABASE_PATH, argument_list=[new_permissions, api_key],
            mode='modify', execute='execute')
    elif args.delete:
        _execute_sqlite(
            '''
            DELETE FROM api_keys
            WHERE api_key=?
            ''', DATABASE_PATH, argument_list=[api_key],
            mode='modify', execute='execute')
