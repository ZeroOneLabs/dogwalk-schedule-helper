from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import BoxLayout


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            MDRectangleFlatButton(
                text="Hello, World 2",
                pos_hint={"center_x": 0.5, "center_y": 0.75},
            )            
        )
        return screen


MainApp().run()