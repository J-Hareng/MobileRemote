import socket
# echo-client.py


_HOST = "192.168.2.117"  # The server's hostname or IP address
_PORT = 3001  # The port used by the server
data = "data"


class C_socket:
    def __init__(self, HOST="192.168.2.117", PORT=3001):

        self.host = HOST
        self.port = PORT
        self.socket = None

    def send_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(b"Hello, world TEST")

            data = s.recv(1024)
            print("data on socket: " + data)


def send_data(Host, datatosend):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, 3001))
        s.sendall(datatosend)
        data = s.recv(1024)
        return data
