from sqlite3 import Row

from database.sqlite3.session import SqliteSession
from grpc_tools_package import users_pb2
from repository import UserRepo


class CreateUserService:

    def __init__(self, session: SqliteSession, user_repo: UserRepo):
        self._session = session
        self.user_repo = user_repo

    def execute(self, username: str, age: int) -> int | None:
        with self._session as session:
            id = self.user_repo.create(username=username, age=age)
            session.commit()
        return users_pb2.RegisterUserResponse(id=id)


class GetUsersService:

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def execute(self):
        users = self.user_repo.get() or []
        if users:
            users = list(map(lambda user: users_pb2.UserData(**user), users))
        return users_pb2.UsersResponse(users=users)


class GetUserByIdService:

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def execute(self, id: int):
        user: Row = self.user_repo.get_by_id(id=id) or {}
        return users_pb2.UserByIdResponse(**user)


class UpdateUserService:

    def __init__(self, session: SqliteSession, user_repo: UserRepo):
        self._session = session
        self.user_repo = user_repo

    def data_to_be_updated_exclude_none(self, **kwargs):  # noqa
        return {key: value for key, value in kwargs.items() if value or value != ''}

    def execute(self, id: int, username: str, age: int):
        with self._session as session:
            kw = self.data_to_be_updated_exclude_none(username=username, age=age)
            self.user_repo.update(id=id, **kw)
            session.commit()
        return users_pb2.UpdateUserResponse(status=True)


class DeleteUserService:

    def __init__(self, session: SqliteSession, user_repo: UserRepo):
        self._session = session
        self.user_repo = user_repo

    def execute(self, id: int):
        with self._session as session:
            self.user_repo.delete(id=id)
            session.commit()
        return users_pb2.DeleteUserResponse(status=True)
