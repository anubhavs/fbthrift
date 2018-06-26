#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
import typing as t

from thrift import Thrift
from thrift.protocol.TProtocol import TProtocolBase

__property__ = property  # sometimes `property` is used as a field name

import simple.dependent.ttypes

UTF8STRINGS: bool


class AnEnum(int):
    ONE: t.ClassVar[AnEnum]
    TWO: t.ClassVar[AnEnum]
    THREE: t.ClassVar[AnEnum]
    FOUR: t.ClassVar[AnEnum]

    _VALUES_TO_NAMES: t.ClassVar[t.Dict[AnEnum, str]]
    _NAMES_TO_VALUES: t.ClassVar[t.Dict[str, AnEnum]]


class SimpleException(Thrift.TException):
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        err_code: t.Optional[int] = ...
    ) -> None:
        ...

    @__property__
    def err_code(self) -> int: ...
    @err_code.setter
    def err_code(self, value: t.Optional[int]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @t.overload
    def readFromJson(self, json: t.Dict[str, t.Any], is_text: bool = ...) -> None: ...
    @t.overload
    def readFromJson(self, json: str, is_text: bool = ...) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class MessageException(Thrift.TException):
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        message: t.Optional[str] = ...,
        err_code: t.Optional[int] = ...
    ) -> None:
        ...

    @__property__
    def message(self) -> str: ...
    @message.setter
    def message(self, value: t.Optional[str]) -> None: ...
    @__property__
    def err_code(self) -> int: ...
    @err_code.setter
    def err_code(self, value: t.Optional[int]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @t.overload
    def readFromJson(self, json: t.Dict[str, t.Any], is_text: bool = ...) -> None: ...
    @t.overload
    def readFromJson(self, json: str, is_text: bool = ...) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class SimpleStruct:
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        is_on: t.Optional[bool] = ...,
        tiny_int: int = ...,
        small_int: t.Optional[int] = ...,
        nice_sized_int: t.Optional[int] = ...,
        big_int: t.Optional[int] = ...,
        coarse_real: float = ...,
        precise_real: t.Optional[float] = ...,
        a_str: t.Optional[str] = ...,
        a_bytes: t.Optional[bytes] = ...
    ) -> None:
        ...

    @__property__
    def is_on(self) -> bool: ...
    @is_on.setter
    def is_on(self, value: t.Optional[bool]) -> None: ...
    @__property__
    def tiny_int(self) -> int: ...
    @tiny_int.setter
    def tiny_int(self, value: int) -> None: ...
    @__property__
    def small_int(self) -> t.Optional[int]: ...
    @small_int.setter
    def small_int(self, value: t.Optional[int]) -> None: ...
    @__property__
    def nice_sized_int(self) -> t.Optional[int]: ...
    @nice_sized_int.setter
    def nice_sized_int(self, value: t.Optional[int]) -> None: ...
    @__property__
    def big_int(self) -> int: ...
    @big_int.setter
    def big_int(self, value: t.Optional[int]) -> None: ...
    @__property__
    def coarse_real(self) -> float: ...
    @coarse_real.setter
    def coarse_real(self, value: float) -> None: ...
    @__property__
    def precise_real(self) -> float: ...
    @precise_real.setter
    def precise_real(self, value: t.Optional[float]) -> None: ...
    @__property__
    def a_str(self) -> str: ...
    @a_str.setter
    def a_str(self, value: t.Optional[str]) -> None: ...
    @__property__
    def a_bytes(self) -> t.Optional[bytes]: ...
    @a_bytes.setter
    def a_bytes(self, value: t.Optional[bytes]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @t.overload
    def readFromJson(self, json: t.Dict[str, t.Any], is_text: bool = ...) -> None: ...
    @t.overload
    def readFromJson(self, json: str, is_text: bool = ...) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class ComplexStruct:
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        structOne: t.Optional[SimpleStruct] = ...,
        structTwo: t.Optional[SimpleStruct] = ...,
        an_integer: t.Optional[int] = ...,
        name: t.Optional[str] = ...,
        an_enum: t.Optional[AnEnum] = ...,
        values: t.Optional[t.List[int]] = ...,
        structs: t.Optional[t.List[SimpleStruct]] = ...,
        amap: t.Optional[t.Dict[str, str]] = ...,
        aset: t.Optional[t.Set[str]] = ...,
        item: t.Optional[simple.dependent.ttypes.Item] = ...
    ) -> None:
        ...

    @__property__
    def structOne(self) -> SimpleStruct: ...
    @structOne.setter
    def structOne(self, value: t.Optional[SimpleStruct]) -> None: ...
    @__property__
    def structTwo(self) -> t.Optional[SimpleStruct]: ...
    @structTwo.setter
    def structTwo(self, value: t.Optional[SimpleStruct]) -> None: ...
    @__property__
    def an_integer(self) -> int: ...
    @an_integer.setter
    def an_integer(self, value: t.Optional[int]) -> None: ...
    @__property__
    def name(self) -> str: ...
    @name.setter
    def name(self, value: t.Optional[str]) -> None: ...
    @__property__
    def an_enum(self) -> AnEnum: ...
    @an_enum.setter
    def an_enum(self, value: t.Optional[AnEnum]) -> None: ...
    @__property__
    def values(self) -> t.List[int]: ...
    @values.setter
    def values(self, value: t.Optional[t.List[int]]) -> None: ...
    @__property__
    def structs(self) -> t.List[SimpleStruct]: ...
    @structs.setter
    def structs(self, value: t.Optional[t.List[SimpleStruct]]) -> None: ...
    @__property__
    def amap(self) -> t.Dict[str, str]: ...
    @amap.setter
    def amap(self, value: t.Optional[t.Dict[str, str]]) -> None: ...
    @__property__
    def aset(self) -> t.Set[str]: ...
    @aset.setter
    def aset(self, value: t.Optional[t.Set[str]]) -> None: ...
    @__property__
    def item(self) -> simple.dependent.ttypes.Item: ...
    @item.setter
    def item(self, value: t.Optional[simple.dependent.ttypes.Item]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @t.overload
    def readFromJson(self, json: t.Dict[str, t.Any], is_text: bool = ...) -> None: ...
    @t.overload
    def readFromJson(self, json: str, is_text: bool = ...) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...


class UnionStruct:
    thrift_spec: t.Tuple[t.Optional[t.Tuple[int, int, str, t.Any, t.Optional[int], int]]]
    thrift_field_annotations: t.Dict[int, t.Dict[str, str]]
    thrift_struct_annotations: t.Dict[str, str]

    def __init__(
        self,
        is_a_bool: t.Optional[bool] = ...,
        some_string_goes_here: t.Optional[str] = ...,
        perhaps_a_big_int: t.Optional[int] = ...
    ) -> None:
        ...

    @__property__
    def is_a_bool(self) -> bool: ...
    @is_a_bool.setter
    def is_a_bool(self, value: t.Optional[bool]) -> None: ...
    @__property__
    def some_string_goes_here(self) -> str: ...
    @some_string_goes_here.setter
    def some_string_goes_here(self, value: t.Optional[str]) -> None: ...
    @__property__
    def perhaps_a_big_int(self) -> int: ...
    @perhaps_a_big_int.setter
    def perhaps_a_big_int(self, value: t.Optional[int]) -> None: ...

    def getType(self) -> int: ...

    IS_A_BOOL: int = ...
    SOME_STRING_GOES_HERE: int = ...
    PERHAPS_A_BIG_INT: int = ...

    def get_is_a_bool(self) -> t.Optional[bool]: ...
    def get_some_string_goes_here(self) -> t.Optional[str]: ...
    def get_perhaps_a_big_int(self) -> t.Optional[int]: ...

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @t.overload
    def readFromJson(self, json: t.Dict[str, t.Any], is_text: bool = ...) -> None: ...
    @t.overload
    def readFromJson(self, json: str, is_text: bool = ...) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...
