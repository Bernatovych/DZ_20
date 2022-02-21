from socket import *

ADR = ('127.0.0.1', 55555)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADR)


def server():
    id = 0
    while True:
        client, client_address = SERVER.accept()
        id += 1
        print(f"Client {id} connected!")
        msg = client.recv(1024).decode("utf8")
        print(f'Client {id} massage: {msg}')
        client.send(bytes("ok", "utf8"))
        client.close()
        print(f"Client {id} close!")


if __name__ == "__main__":
    SERVER.listen()
    print("...")
    server()
    SERVER.close()