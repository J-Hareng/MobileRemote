import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import io from "socket.io-client"

class API{
  constructor(props){
    this.socket = io("http://192.168.21.24:8080");
  }
  sendKey(type, key){
    this.socket.emit("cum", "cum")
  }
}
const api = new API();
export default function App() {
  

  
  
  return (
    <View style={styles.container}>
      <Button
        onPress={()=>{api.sendKey("data","ad")}}
        style={{height: 500,
          width: 30, borderwidth:30}}
        title="Learn More"
        color="#841584"
        accessibilityLabel="Learn more about this purple button"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#00000a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  button: {
    height: 30,
    width: 30,
    
  }
});

