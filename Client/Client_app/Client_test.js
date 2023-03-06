import TcpSocket from 'react-native-tcp-socket';
var net = require('net');

export const test = function(){
  var client = net.createConnection(3001);

  client.on('error', function(error) {
    console.log(error)
  });
  
  client.on('data', function(data) {
    console.log('message was received', data)
  });
  
}



