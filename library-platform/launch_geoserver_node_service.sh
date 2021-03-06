#!/bin/bash
set -a
source stac_envs &&
    python3 geoserver_node_drive_mirror_service.py --app_port ${GEOSERVER_HEALTH_PORT} --snapshot_pattern ${GEOSERVER_SNAPSHOT_PATTERN} --mount_point ${GEOSERVER_DATA_DISK_VOLUME} --mem_size ${GEOSERVER_MAX_RAM} --check_time 300 --geoserver_service_name geoserver --google_cloud_zone ${GOOGLE_CLOUD_ZONE}
