from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class MeatSelection(GridLayout):
    pass


class RotiParfaitApp(App):
    def build(self):
        return MeatSelection()

if __name__ == '__main__':
    RotiParfaitApp().run()