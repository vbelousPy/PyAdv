import socket
import threading


def msg_listener(some_client, some_address):
    while True:
        data = some_client.recv(1024)
        if data:
            with open("1.txt", "a+") as f:
                f.write("<{}> - <{}>".format(some_address, data.decode()))
                f.flush()
                break


def wait_connect(s_socket):
    while True:
        client, address = s_socket.accept()
        client.settimeout(60)
        threading.Thread(target=msg_listener, args=(client, address)).start()


server_socket = socket.socket()
server_socket.bind(("", 9000))
server_socket.listen(2)
threading.Thread(target=wait_connect, args=(server_socket,)).start()

def client_writer(some_client):
    some_text = ""
    while not some_text == "q":
        some_text = input("Enter msg: ")
        some_client.send(str.encode(some_text))
    some_client.close()


client_socket = socket.socket()
client_socket.connect(("localhost", 9000))
threading.Thread(target=client_writer, args=(client_socket,)).start()

