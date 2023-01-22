from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
class Formularz(GridLayout):
    def __init__(self, **kwargs):
        super(Formularz, self).__init__(**kwargs)
        
        self.cols = 2
        self.label = self.add_widget(Label(text="To jest etykieta ", font_size = "30sp"))
        self.name = TextInput(multiline=False, font_size="30sp")
        self.name.background_color = [1, 1, 0, 1]
        self.add_widget(self.name)
        self.img =Image(source="rys.png")
        
        self.add_widget(self.img)
        self.submit = Button(text = "Wyślij", font_size = "32sp")
        self.submit.background_color = [1, 0, 0, 1]
        self.add_widget(self.submit)
class MobileApp(App):
   def build(self):
      return Formularz()

if __name__ == '__main__':
   MobileApp().run()
