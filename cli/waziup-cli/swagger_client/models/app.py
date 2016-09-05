# coding: utf-8

"""
    WAZIUP API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class App(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, id=None, owner=None, updated=None, url=None, uuid=None):
        """
        App - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'str',
            'id': 'str',
            'owner': 'str',
            'updated': 'str',
            'url': 'str',
            'uuid': 'str'
        }

        self.attribute_map = {
            'created': 'Created',
            'id': 'ID',
            'owner': 'Owner',
            'updated': 'Updated',
            'url': 'URL',
            'uuid': 'UUID'
        }

        self._created = created
        self._id = id
        self._owner = owner
        self._updated = updated
        self._url = url
        self._uuid = uuid

    @property
    def created(self):
        """
        Gets the created of this App.


        :return: The created of this App.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this App.


        :param created: The created of this App.
        :type: str
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this App.


        :return: The id of this App.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this App.


        :param id: The id of this App.
        :type: str
        """

        self._id = id

    @property
    def owner(self):
        """
        Gets the owner of this App.


        :return: The owner of this App.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this App.


        :param owner: The owner of this App.
        :type: str
        """

        self._owner = owner

    @property
    def updated(self):
        """
        Gets the updated of this App.


        :return: The updated of this App.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this App.


        :param updated: The updated of this App.
        :type: str
        """

        self._updated = updated

    @property
    def url(self):
        """
        Gets the url of this App.


        :return: The url of this App.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this App.


        :param url: The url of this App.
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """
        Gets the uuid of this App.


        :return: The uuid of this App.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this App.


        :param uuid: The uuid of this App.
        :type: str
        """

        self._uuid = uuid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other