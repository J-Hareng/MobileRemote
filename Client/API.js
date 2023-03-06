// const { connect } = require('node:http2');
var net = require('node:net');

//192.168.2.117
//127.0.0.1 !!

var HOST = '192.168.2.117';
var localhost = '127.0.0.1';


var PORT = 3001;


    
class Own_client{
  constructor(){
    this.host = localhost
    this.port = 3001;
    this.client = new net.Socket();
    
  }
  
   connect(){
    this.client.connect(this.port, this.host, function() {
    console.log('CONNECTED TO: ' + this.port + ':' + this.host);
    });
  }
  
  close() {
    this.client.on('close', function() {  // Add a 'close' event handler for the client socket
      console.log('Connection closed');
    });
    this.client.destroy();
  }
  
   send(data_to_send){
  //sending
  this.client.write(data_to_send); 
    console.log("data sent: " + data_to_send)
    
    //recieving
    this.client.on('data', function(data) {
        if(data == "CLOSE"){
          
        }
        console.log('DATA: ' + data)
        
      });
  }

}


// let _client = new Own_client();
// function main(){
//     _client.connect();
//     _client.send("Vdown")
//     setTimeout(function() {
//       _client.close();
//   }, 100);
// }

// main();

class Own_client{
  constructor(){
    this.host = HOST
    this.port = 3001;
    this.client = new net.Socket();
    
  }
  
   connect(){
    this.client.connect(this.port, this.host, function() {
    console.log('CONNECTED TO: ' + this.port + ':' + this.host);
    });
  }
  
  close() {
    this.client.on('close', function() {  // Add a 'close' event handler for the client socket
      console.log('Connection closed');
    });
    this.client.destroy();
  }
  
   send(data_to_send){
  //sending
  this.client.write(data_to_send); 
    console.log("data sent: " + data_to_send)
    
    //recieving
    this.client.on('data', function(data) {
        if(data == "CLOSE"){
          
        }
        console.log('DATA: ' + data)
        
      });
  }

}