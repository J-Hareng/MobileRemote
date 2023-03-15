import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class MyApp(App):  # <- Main Class
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()


# import kivy
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# import esocket as sock

# kivy.require("2.0.0")
# # ipadresses:
# # Laptop in hotspot = 192.168.147.24


# class MyRoot(BoxLayout):

#     def __init__(self):
#         super(MyRoot, self).__init__()

#     def send_message(self, a):
#         print("button pressed")
#         data = sock.send_data("192.168.147.24", b"hiu hui hui")
#         print(data)
#         return

#     builder.lo
# # self.random_label.text = data


# class MainApp(App):

#     def build(self):
#         return MyRoot()


# mainApp = MainApp()
# mainApp.run()
