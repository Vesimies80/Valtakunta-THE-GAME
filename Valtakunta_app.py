import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

roles = ["kansalainen", "kurtesaani", "orja", "aatelinen", "hallitsija"]

class ConfigWindow(Screen):
    player_name = ObjectProperty(None)
    role = ObjectProperty(None)

    _players = []

    def submitbtn(self):
        if self.player_name.text != "" and self.role.text != "":
            if self.role.text.lower() not in roles:
                invalidRole()
            else:
                _players.append((self.player_name.text, self.role.text))
                self.reset()

    def start_game(login):
        self.reset()
        sm.current = "config"

    def reset(self):
        self.player_name.text = ""
        self.role.text = ""

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

def invalidRole():
    pop = Popup(title="Invalid Role", content=Label(text='The inputted role is invalid try: kansalainen, kurtesaani, orja, aatelinen, hallitsija'), size_hint=(1,1))
    pop.open()

kv = Builder.load_file("valtakunta.kv")
sm = WindowManager()
screens = [ConfigWindow(name="config")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "config"

class ValtakuntaApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    ValtakuntaApp().run()