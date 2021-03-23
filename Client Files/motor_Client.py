import socket
from main_Movement import movement


def init():
    #CREATES SOCKET
    connecting = True
    HOST = '192.168.20.136'
    #EDIT THIS AND SET TO IP OF SERVER AKA THE COMPUTER RUNNING INTERFACE
    PORT = 4242
    while connecting:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST,PORT))
            print("Binded %s:%s" % (HOST,PORT))
            client_socket.sendall(b'motor_client')
            connecting = False
            return client_socket
        except:
            print("failed to connect")
def main():
    sock = init()
    connected = True
    while connected:
        input = sock.recv(4092)
        data = input.decode()
        if data == "esc":
            movement('esc')
            sock.close()
            connected = False
        elif "None" not in data:
            movement(data)
        else:
            pass
main()
