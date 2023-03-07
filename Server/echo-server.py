from aiohttp import web
import socketio

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)


@sio.on('cum')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: ", sid)
    print(message)

# We bind our aiohttp endpoint to our app
# router

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)
