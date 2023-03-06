import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

import NetInfo from '@react-native-community/netinfo';
const { Socket } = require("react-native-tcp-socket");

async function getdata() {
  const socket = new Socket();
  
  NetInfo.fetch().then(state => {
  console.log(state)
    if (state.isConnected) {
    console.log(socket)
      socket.connect('192.168.2.117', 3001, function test() {
        console.log('Connected to server');
        socket.write('Hello server!');
        
        socket.on('data', data => {
          console.log('Received data from server:', data.toString());
          socket.destroy(); // Close the connection after receiving data
        });
      });
    } else {
      console.log('Not connected to the internet');
    }
  });
}


export default function App() {  
  getdata();
  
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

