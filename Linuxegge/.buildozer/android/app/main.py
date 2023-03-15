import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import esocket as sock

kivy.require("2.0.0")
# ipadresses:
# Laptop in hotspot = 192.168.147.24


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def send_message(self, a):
        print("button pressed")
        data = sock.send_data("192.168.147.24", b"hiu hui hui")
        print(data)
        return
# self.random_label.text = data


class MainApp(App):

    def build(self):
        return MyRoot()


mainApp = MainApp()
mainApp.run()
