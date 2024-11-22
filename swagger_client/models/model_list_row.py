# coding: utf-8

"""
    База кроссов автозапчастей FAPI. Описание доступа через API

    База кроссов автозапчастей FAPI. Описание доступа через API  # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: development.iisis@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelListRow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'i': 'int',
        'dbi': 'int',
        'mfi': 'int',
        'd': 'str',
        'cb': 'int',
        'ce': 'int'
    }

    attribute_map = {
        'i': 'i',
        'dbi': 'dbi',
        'mfi': 'mfi',
        'd': 'd',
        'cb': 'cb',
        'ce': 'ce'
    }

    def __init__(self, i=None, dbi=None, mfi=None, d=None, cb=None, ce=None):  # noqa: E501
        """ModelListRow - a model defined in Swagger"""  # noqa: E501

        self._i = None
        self._dbi = None
        self._mfi = None
        self._d = None
        self._cb = None
        self._ce = None
        self.discriminator = None

        self.i = i
        self.dbi = dbi
        self.mfi = mfi
        self.d = d
        self.cb = cb
        self.ce = ce

    @property
    def i(self):
        """Gets the i of this ModelListRow.  # noqa: E501

        Index / Индекс  # noqa: E501

        :return: The i of this ModelListRow.  # noqa: E501
        :rtype: int
        """
        return self._i

    @i.setter
    def i(self, i):
        """Sets the i of this ModelListRow.

        Index / Индекс  # noqa: E501

        :param i: The i of this ModelListRow.  # noqa: E501
        :type: int
        """
        if i is None:
            raise ValueError("Invalid value for `i`, must not be `None`")  # noqa: E501

        self._i = i

    @property
    def dbi(self):
        """Gets the dbi of this ModelListRow.  # noqa: E501

        Index / Индекс  # noqa: E501

        :return: The dbi of this ModelListRow.  # noqa: E501
        :rtype: int
        """
        return self._dbi

    @dbi.setter
    def dbi(self, dbi):
        """Sets the dbi of this ModelListRow.

        Index / Индекс  # noqa: E501

        :param dbi: The dbi of this ModelListRow.  # noqa: E501
        :type: int
        """
        if dbi is None:
            raise ValueError("Invalid value for `dbi`, must not be `None`")  # noqa: E501

        self._dbi = dbi

    @property
    def mfi(self):
        """Gets the mfi of this ModelListRow.  # noqa: E501

        Manufacturer index / Ссылка на производителя (внешний ключ на manufacturerList.i)  # noqa: E501

        :return: The mfi of this ModelListRow.  # noqa: E501
        :rtype: int
        """
        return self._mfi

    @mfi.setter
    def mfi(self, mfi):
        """Sets the mfi of this ModelListRow.

        Manufacturer index / Ссылка на производителя (внешний ключ на manufacturerList.i)  # noqa: E501

        :param mfi: The mfi of this ModelListRow.  # noqa: E501
        :type: int
        """
        if mfi is None:
            raise ValueError("Invalid value for `mfi`, must not be `None`")  # noqa: E501

        self._mfi = mfi

    @property
    def d(self):
        """Gets the d of this ModelListRow.  # noqa: E501

        Описание  # noqa: E501

        :return: The d of this ModelListRow.  # noqa: E501
        :rtype: str
        """
        return self._d

    @d.setter
    def d(self, d):
        """Sets the d of this ModelListRow.

        Описание  # noqa: E501

        :param d: The d of this ModelListRow.  # noqa: E501
        :type: str
        """
        if d is None:
            raise ValueError("Invalid value for `d`, must not be `None`")  # noqa: E501

        self._d = d

    @property
    def cb(self):
        """Gets the cb of this ModelListRow.  # noqa: E501

        Начало выпуска (unix time)  # noqa: E501

        :return: The cb of this ModelListRow.  # noqa: E501
        :rtype: int
        """
        return self._cb

    @cb.setter
    def cb(self, cb):
        """Sets the cb of this ModelListRow.

        Начало выпуска (unix time)  # noqa: E501

        :param cb: The cb of this ModelListRow.  # noqa: E501
        :type: int
        """
        if cb is None:
            raise ValueError("Invalid value for `cb`, must not be `None`")  # noqa: E501

        self._cb = cb

    @property
    def ce(self):
        """Gets the ce of this ModelListRow.  # noqa: E501

        Окончание выпуска (unix time)  # noqa: E501

        :return: The ce of this ModelListRow.  # noqa: E501
        :rtype: int
        """
        return self._ce

    @ce.setter
    def ce(self, ce):
        """Sets the ce of this ModelListRow.

        Окончание выпуска (unix time)  # noqa: E501

        :param ce: The ce of this ModelListRow.  # noqa: E501
        :type: int
        """
        if ce is None:
            raise ValueError("Invalid value for `ce`, must not be `None`")  # noqa: E501

        self._ce = ce

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ModelListRow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelListRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
