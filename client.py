from socket import *
from threading import Thread

ADR = ('127.0.0.1', 55555)


def client():
    print('Connected!')
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADR)
    client_socket.send(bytes('Hi!', "utf8"))
    msg = client_socket.recv(1024).decode("utf8")
    if msg == "ok":
        print(f'Server: {msg}')
        print('close')
        client_socket.close()


receive_thread = Thread(target=client)
receive_thread1 = Thread(target=client)
receive_thread.start()
receive_thread.join()
receive_thread1.start()
receive_thread1.join()