from concurrent import futures

import grpc

from database.sqlite3.session import SqliteSession
from database.sqlite3.sqlite_engine import SqliteEngine
from grpc_tools_package import users_pb2_grpc
from grpc_tools_package.users_pb2_grpc import UsersServiceServicer
from repository import UserRepo
from users_aplication_service import (
    CreateUserService,
    DeleteUserService,
    GetUserByIdService,
    GetUsersService,
    UpdateUserService,
)


class UsersServiceServicerImpl(UsersServiceServicer):

    def __init__(self, user_repo: UserRepo, session: SqliteSession):
        self.user_repo = user_repo
        self.session = session

    def GetUsers(self, request, context):
        service = GetUsersService(user_repo=self.user_repo)
        return service.execute()

    def GetUserById(self, request, context):
        service = GetUserByIdService(user_repo=self.user_repo)
        return service.execute(id=request.id)

    def CreateUser(self, request, context):
        service = CreateUserService(session=self.session, user_repo=self.user_repo)
        return service.execute(username=request.username, age=request.age)

    def UpdateUser(self, request, context):
        service = UpdateUserService(session=self.session, user_repo=self.user_repo)
        return service.execute(id=request.id, username=request.username, age=request.age)

    def DeleteUser(self, request, context):
        service = DeleteUserService(session=self.session, user_repo=self.user_repo)
        return service.execute(id=request.id)


def serve():
    # Dependencies
    engine = SqliteEngine(path='./mydb.db')
    session_adapter = SqliteSession(engine=engine)
    user_repo = UserRepo(session=session_adapter)

    # Start Grpc Server
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServiceServicer_to_server(
        UsersServiceServicerImpl(user_repo=user_repo, session=session_adapter), grpc_server,
    )
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()

    print("GRPC Server is running...")
    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if '__main__' == __name__:
    serve()
