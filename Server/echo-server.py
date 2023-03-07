from aiohttp import web
import socketio

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no change


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for


@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: ", sid)
    print(message)

# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)


# import socket
# import subprocess
# HOST = ''
# PORT = 3001
# # def get_data(client_sock):
# def Usedata(data):
#     return;
# def start_server():
#     Active = True
#     while Active:
#         for i in range(10):
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#                 sock.bind((HOST, PORT))
#                 sock.listen()
#                 conn, address = sock.accept()
#                 with conn as conn_sock:
#                     print(f"got connection from {address}")
#                     connection = True
#                     while connection:
#                         try:
#                             data = conn_sock.recv(1024)
#                             if not data:
#                                 break;
#                             print(f"received-in-server: {data}")
#                             if(data == b"Vup"):
#                                 print ("Volume Up")
#                                 subprocess.call([r'C:\Users\flits\Desktop\Code\Neuer Ordner\privat\Server\batches\VolUp.bat'])
#                             elif(data == b"Vdown"):
#                                 print ("Volume Down")
#                                 subprocess.call([r'C:\Users\flits\Desktop\Code\Neuer Ordner\privat\Server\batches\VolDown.bat'])
#                             elif data == b"Stop":
#                                 Active = False
#                                 return;
#                             elif data == b"close":
#                                 conn_sock.sendall("CLOSE")
#                                 connection = False
#                             else:
#                                 conn_sock.sendall(b"Sucess//. Data received: " + data)
#                         except ConnectionResetError:
#                             connection = False
#                             print("Connection lost")
# if __name__ == '__main__':
#     start_server();
