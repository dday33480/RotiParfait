from format_time import TimeConversion
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from meats import InputDetails
from time_calculation import Calculation

class MeatSelection(Screen):

    btn_down = BooleanProperty(False)

    def on_toggle_button_state(self, button):     

        if button.state == "normal":
            self.btn_down = False
        else:
            self.btn_down = True

        print("toggle state: " + button.state) 

    
    def meat_selection(self):

        chicken = self.ids.Chicken
        beef = self.ids.Beef
        lamb = self.ids.Lamb
        pig = self.ids.Pig

        meat = ""
        if chicken.state == "down":
            meat = "Poulet"
        elif beef.state == "down":
            meat = "Boeuf"
        elif lamb.state == "down":
            meat = "Agneau"
        elif pig.state == "down":
            meat = "Porc"
        else:
            meat = "Pas de viande sélectionnée"

        print("meat selected: " + meat)

        meat_time = InputDetails.get_meat_input(meat)
        time = float(meat_time)

        print(f"meat_time var Time: {meat_time}")
        print(f"time var Time: {time}")

        manager = App.get_running_app().root
        manager.time_var = time


class WeightSelection(Screen):

    def weight_input(self):
        kilo_input = self.ids.kilo.text
        grammes_input = self.ids.grammes.text

        kilo_text = kilo_input
        grammes_text = grammes_input

        weight_kg = int(kilo_text)*1000
        weight_gr = int(grammes_text)
        weight_concat = weight_kg + weight_gr
        weight = float(weight_concat/1000)

        print(weight_concat)
        print(weight)

        manager = App.get_running_app().root
        manager.weight_var = weight
    
    input_weight = weight_input

    print(input_weight)



class ResultWindow(Screen):

    cooking_time = StringProperty("0:00")

    def final_result(self):
        manager = App.get_running_app().root
        time = manager.time_var
        weight = manager.weight_var
        print(f"Time: {time}")
        print(f"Weight: {weight}")
        time_calc = Calculation.cooking_time_calc(time, weight)
        result = TimeConversion.cooking_time_formatted(time_calc)
        print(f"time_calc: {time_calc}")
        print(result)
        self.cooking_time = result

    

class WindowManager(ScreenManager):
    time_var = 0.0
    weight_var = 0.0




kv = Builder.load_file("rotiparfait.kv")

class RotiParfaitApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RotiParfaitApp().run()