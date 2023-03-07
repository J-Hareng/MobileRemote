// init server
const express = require('express');
const { Socket } = require('socket.io');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

const port = 3001

io.on("connection", socket => {
    console.log("User conectet on socket: ");
    console.log(socket.handshake.address);
    socket.on("Kevent", event =>{
        console.log(event)
    })
})


server.listen(port, ()=> console.log("server listening on port: " + port));