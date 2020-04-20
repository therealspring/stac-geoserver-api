# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.any_of_ur_istring import AnyOfURIstring
from openapi_server.models.link import Link
from openapi_server import util

from openapi_server.models.any_of_ur_istring import AnyOfURIstring  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501

class LandingPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, description=None, links=None, stac_version=None, stac_extensions=None, id=None):  # noqa: E501
        """LandingPage - a model defined in OpenAPI

        :param title: The title of this LandingPage.  # noqa: E501
        :type title: str
        :param description: The description of this LandingPage.  # noqa: E501
        :type description: str
        :param links: The links of this LandingPage.  # noqa: E501
        :type links: List[Link]
        :param stac_version: The stac_version of this LandingPage.  # noqa: E501
        :type stac_version: str
        :param stac_extensions: The stac_extensions of this LandingPage.  # noqa: E501
        :type stac_extensions: List[AnyOfURIstring]
        :param id: The id of this LandingPage.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'title': str,
            'description': str,
            'links': List[Link],
            'stac_version': str,
            'stac_extensions': List[AnyOfURIstring],
            'id': str
        }

        self.attribute_map = {
            'title': 'title',
            'description': 'description',
            'links': 'links',
            'stac_version': 'stac_version',
            'stac_extensions': 'stac_extensions',
            'id': 'id'
        }

        self._title = title
        self._description = description
        self._links = links
        self._stac_version = stac_version
        self._stac_extensions = stac_extensions
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'LandingPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The landingPage of this LandingPage.  # noqa: E501
        :rtype: LandingPage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this LandingPage.


        :return: The title of this LandingPage.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LandingPage.


        :param title: The title of this LandingPage.
        :type title: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this LandingPage.


        :return: The description of this LandingPage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LandingPage.


        :param description: The description of this LandingPage.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def links(self):
        """Gets the links of this LandingPage.


        :return: The links of this LandingPage.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LandingPage.


        :param links: The links of this LandingPage.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def stac_version(self):
        """Gets the stac_version of this LandingPage.


        :return: The stac_version of this LandingPage.
        :rtype: str
        """
        return self._stac_version

    @stac_version.setter
    def stac_version(self, stac_version):
        """Sets the stac_version of this LandingPage.


        :param stac_version: The stac_version of this LandingPage.
        :type stac_version: str
        """
        if stac_version is None:
            raise ValueError("Invalid value for `stac_version`, must not be `None`")  # noqa: E501

        self._stac_version = stac_version

    @property
    def stac_extensions(self):
        """Gets the stac_extensions of this LandingPage.


        :return: The stac_extensions of this LandingPage.
        :rtype: List[AnyOfURIstring]
        """
        return self._stac_extensions

    @stac_extensions.setter
    def stac_extensions(self, stac_extensions):
        """Sets the stac_extensions of this LandingPage.


        :param stac_extensions: The stac_extensions of this LandingPage.
        :type stac_extensions: List[AnyOfURIstring]
        """

        self._stac_extensions = stac_extensions

    @property
    def id(self):
        """Gets the id of this LandingPage.


        :return: The id of this LandingPage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LandingPage.


        :param id: The id of this LandingPage.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id