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

from swagger_client.models.modification_list_row_p import ModificationListRowP  # noqa: F401,E501


class ModificationListRow(object):
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
        'mdi': 'int',
        'd': 'str',
        'fd': 'str',
        'cb': 'int',
        'ce': 'int',
        'engine_type': 'str',
        'engine_code': 'str',
        'power': 'str',
        'capacity': 'str',
        'drive_type': 'str',
        'body_type': 'str',
        'p': 'ModificationListRowP'
    }

    attribute_map = {
        'i': 'i',
        'dbi': 'dbi',
        'mdi': 'mdi',
        'd': 'd',
        'fd': 'fd',
        'cb': 'cb',
        'ce': 'ce',
        'engine_type': 'engineType',
        'engine_code': 'engineCode',
        'power': 'power',
        'capacity': 'capacity',
        'drive_type': 'driveType',
        'body_type': 'bodyType',
        'p': 'p'
    }

    def __init__(self, i=None, dbi=None, mdi=None, d=None, fd=None, cb=None, ce=None, engine_type=None, engine_code=None, power=None, capacity=None, drive_type=None, body_type=None, p=None):  # noqa: E501
        """ModificationListRow - a model defined in Swagger"""  # noqa: E501

        self._i = None
        self._dbi = None
        self._mdi = None
        self._d = None
        self._fd = None
        self._cb = None
        self._ce = None
        self._engine_type = None
        self._engine_code = None
        self._power = None
        self._capacity = None
        self._drive_type = None
        self._body_type = None
        self._p = None
        self.discriminator = None

        self.i = i
        self.dbi = dbi
        self.mdi = mdi
        self.d = d
        self.fd = fd
        self.cb = cb
        self.ce = ce
        self.engine_type = engine_type
        self.engine_code = engine_code
        self.power = power
        self.capacity = capacity
        self.drive_type = drive_type
        self.body_type = body_type
        self.p = p

    @property
    def i(self):
        """Gets the i of this ModificationListRow.  # noqa: E501

        Index / Индекс  # noqa: E501

        :return: The i of this ModificationListRow.  # noqa: E501
        :rtype: int
        """
        return self._i

    @i.setter
    def i(self, i):
        """Sets the i of this ModificationListRow.

        Index / Индекс  # noqa: E501

        :param i: The i of this ModificationListRow.  # noqa: E501
        :type: int
        """
        if i is None:
            raise ValueError("Invalid value for `i`, must not be `None`")  # noqa: E501

        self._i = i

    @property
    def dbi(self):
        """Gets the dbi of this ModificationListRow.  # noqa: E501

        Index / Индекс  # noqa: E501

        :return: The dbi of this ModificationListRow.  # noqa: E501
        :rtype: int
        """
        return self._dbi

    @dbi.setter
    def dbi(self, dbi):
        """Sets the dbi of this ModificationListRow.

        Index / Индекс  # noqa: E501

        :param dbi: The dbi of this ModificationListRow.  # noqa: E501
        :type: int
        """
        if dbi is None:
            raise ValueError("Invalid value for `dbi`, must not be `None`")  # noqa: E501

        self._dbi = dbi

    @property
    def mdi(self):
        """Gets the mdi of this ModificationListRow.  # noqa: E501

        Model index / Ссылка на Модель автомобиля (внешний ключ на model.i)  # noqa: E501

        :return: The mdi of this ModificationListRow.  # noqa: E501
        :rtype: int
        """
        return self._mdi

    @mdi.setter
    def mdi(self, mdi):
        """Sets the mdi of this ModificationListRow.

        Model index / Ссылка на Модель автомобиля (внешний ключ на model.i)  # noqa: E501

        :param mdi: The mdi of this ModificationListRow.  # noqa: E501
        :type: int
        """
        if mdi is None:
            raise ValueError("Invalid value for `mdi`, must not be `None`")  # noqa: E501

        self._mdi = mdi

    @property
    def d(self):
        """Gets the d of this ModificationListRow.  # noqa: E501

        Описание  # noqa: E501

        :return: The d of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._d

    @d.setter
    def d(self, d):
        """Sets the d of this ModificationListRow.

        Описание  # noqa: E501

        :param d: The d of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if d is None:
            raise ValueError("Invalid value for `d`, must not be `None`")  # noqa: E501

        self._d = d

    @property
    def fd(self):
        """Gets the fd of this ModificationListRow.  # noqa: E501

        Описание  # noqa: E501

        :return: The fd of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._fd

    @fd.setter
    def fd(self, fd):
        """Sets the fd of this ModificationListRow.

        Описание  # noqa: E501

        :param fd: The fd of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if fd is None:
            raise ValueError("Invalid value for `fd`, must not be `None`")  # noqa: E501

        self._fd = fd

    @property
    def cb(self):
        """Gets the cb of this ModificationListRow.  # noqa: E501

        Дата начала сборки (UNIX TIME)  # noqa: E501

        :return: The cb of this ModificationListRow.  # noqa: E501
        :rtype: int
        """
        return self._cb

    @cb.setter
    def cb(self, cb):
        """Sets the cb of this ModificationListRow.

        Дата начала сборки (UNIX TIME)  # noqa: E501

        :param cb: The cb of this ModificationListRow.  # noqa: E501
        :type: int
        """
        if cb is None:
            raise ValueError("Invalid value for `cb`, must not be `None`")  # noqa: E501

        self._cb = cb

    @property
    def ce(self):
        """Gets the ce of this ModificationListRow.  # noqa: E501

        Дата окончания сборки (UNIX TIME)  # noqa: E501

        :return: The ce of this ModificationListRow.  # noqa: E501
        :rtype: int
        """
        return self._ce

    @ce.setter
    def ce(self, ce):
        """Sets the ce of this ModificationListRow.

        Дата окончания сборки (UNIX TIME)  # noqa: E501

        :param ce: The ce of this ModificationListRow.  # noqa: E501
        :type: int
        """
        if ce is None:
            raise ValueError("Invalid value for `ce`, must not be `None`")  # noqa: E501

        self._ce = ce

    @property
    def engine_type(self):
        """Gets the engine_type of this ModificationListRow.  # noqa: E501

        Тип двигателя  # noqa: E501

        :return: The engine_type of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this ModificationListRow.

        Тип двигателя  # noqa: E501

        :param engine_type: The engine_type of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if engine_type is None:
            raise ValueError("Invalid value for `engine_type`, must not be `None`")  # noqa: E501

        self._engine_type = engine_type

    @property
    def engine_code(self):
        """Gets the engine_code of this ModificationListRow.  # noqa: E501

        Код двигателя  # noqa: E501

        :return: The engine_code of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._engine_code

    @engine_code.setter
    def engine_code(self, engine_code):
        """Sets the engine_code of this ModificationListRow.

        Код двигателя  # noqa: E501

        :param engine_code: The engine_code of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if engine_code is None:
            raise ValueError("Invalid value for `engine_code`, must not be `None`")  # noqa: E501

        self._engine_code = engine_code

    @property
    def power(self):
        """Gets the power of this ModificationListRow.  # noqa: E501

        Мощность  # noqa: E501

        :return: The power of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this ModificationListRow.

        Мощность  # noqa: E501

        :param power: The power of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if power is None:
            raise ValueError("Invalid value for `power`, must not be `None`")  # noqa: E501

        self._power = power

    @property
    def capacity(self):
        """Gets the capacity of this ModificationListRow.  # noqa: E501

        Объем  # noqa: E501

        :return: The capacity of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ModificationListRow.

        Объем  # noqa: E501

        :param capacity: The capacity of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if capacity is None:
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def drive_type(self):
        """Gets the drive_type of this ModificationListRow.  # noqa: E501

        Тип привода  # noqa: E501

        :return: The drive_type of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._drive_type

    @drive_type.setter
    def drive_type(self, drive_type):
        """Sets the drive_type of this ModificationListRow.

        Тип привода  # noqa: E501

        :param drive_type: The drive_type of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if drive_type is None:
            raise ValueError("Invalid value for `drive_type`, must not be `None`")  # noqa: E501

        self._drive_type = drive_type

    @property
    def body_type(self):
        """Gets the body_type of this ModificationListRow.  # noqa: E501

        Тип кузова  # noqa: E501

        :return: The body_type of this ModificationListRow.  # noqa: E501
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this ModificationListRow.

        Тип кузова  # noqa: E501

        :param body_type: The body_type of this ModificationListRow.  # noqa: E501
        :type: str
        """
        if body_type is None:
            raise ValueError("Invalid value for `body_type`, must not be `None`")  # noqa: E501

        self._body_type = body_type

    @property
    def p(self):
        """Gets the p of this ModificationListRow.  # noqa: E501


        :return: The p of this ModificationListRow.  # noqa: E501
        :rtype: ModificationListRowP
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this ModificationListRow.


        :param p: The p of this ModificationListRow.  # noqa: E501
        :type: ModificationListRowP
        """
        if p is None:
            raise ValueError("Invalid value for `p`, must not be `None`")  # noqa: E501

        self._p = p

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
        if issubclass(ModificationListRow, dict):
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
        if not isinstance(other, ModificationListRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other