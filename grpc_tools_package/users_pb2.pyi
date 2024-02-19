from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserByIdResponse(_message.Message):
    __slots__ = ["id", "username", "age", "created_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    age: int
    created_at: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., age: _Optional[int] = ..., created_at: _Optional[str] = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ["id", "username", "age", "created_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    age: int
    created_at: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., age: _Optional[int] = ..., created_at: _Optional[str] = ...) -> None: ...

class UsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserData]
    def __init__(self, users: _Optional[_Iterable[_Union[UserData, _Mapping]]] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ["id", "username", "age"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    age: int
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["id", "username", "age"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    age: int
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
