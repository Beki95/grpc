import grpc

from grpc_tools_package import (
    users_pb2,
    users_pb2_grpc,
)


def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersServiceStub(channel)

        user = stub.GetUserById(users_pb2.UserByIdRequest(id=2))
        print(user.username)

        users = stub.GetUsers(users_pb2.Empty())
        print(users)

        # id = stub.CreateUser(users_pb2.RegisterUserRequest(username='BitMan', age=23))
        # print(id)

        # del_response = stub.DeleteUser(users_pb2.DeleteUserRequest(id=0))
        # print(del_response)

        # up_response = stub.UpdateUser(users_pb2.UpdateUserRequest(id=2, username='Albert'))
        # print(up_response)


if __name__ == '__main__':
    client()
