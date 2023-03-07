import socketio
from gevent.pywsgi import WSGIServer

# create a Socket.IO server instance
sio = socketio.AsyncServer()

# define a function to be called when data is received


@sio.on('data')
async def handle_data(sid, data):
    print('Received data:', data)

# create a Socket.IO app instance and attach the server to it
app = socketio.WSGIApp(sio)

# start the server
if __name__ == '__main__':
    port = 3001
    print(f'Starting server on port {port}')
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()
