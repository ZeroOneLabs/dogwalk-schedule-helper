from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

import dog_weather

# On load and button press: Load weather data func
def load_weather_data():
    # INIT UI elements (clear text from all fields)
    # Get weather data
    
    # Populate UI elements
    pass


class ConverterApp(MDApp):
    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        wdata = dog_weather.get_weather_data()

        self.toolbar = MDToolbar(title="Happy Paws")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)

        for day in wdata:
            time = day["morning_walks"][0]["time"]
            desc = day["morning_walks"][0]["desc"]

            self.label = MDLabel(
                text = f"{time} - {desc}",
                halign = "center",
                pos_hint = { "center_x": 0.5, "center_y": 0.85 } 
            )
            screen.add_widget(self.label)
            break

        self.label = MDLabel(
            text = "10AM = Good",
            halign = "center",
            pos_hint = { "center_x": 0.5, "center_y": 0.75 } 
        )
        screen.add_widget(self.label)
        
        return screen

if __name__ == '__main__':
    ConverterApp().run()