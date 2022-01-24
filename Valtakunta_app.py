import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

roles = ["kansalainen", "kurtesaani", "orja", "aatelinen", "hallitsija"]

class ConfigWindow(Screen):
    player_name = ObjectProperty(None)
    role = ObjectProperty(None)

    _players = []

    def submitbtn(self):
        if self.player_name.text != "" and self.role.text != "":
            if self.role.text.lower() not in roles:
                content=Button(text="The inputted role is invalid try: \nkansalainen, kurtesaani, orja, aatelinen, hallitsija")
                pop = Popup(title='Invalid Role',content=content, auto_dismiss=False)
                content.bind(on_press=pop.dismiss)
                pop.open()

            else:
                self._players.append((self.player_name.text, self.role.text))
                self.reset()

    def start_game(self):
        if len(self._players) == 0:
            content=Button(text="No players inputted")
            pop = Popup(title='No players',content=content, auto_dismiss=False)
            content.bind(on_press=pop.dismiss)
            pop.open()
        else:
            self.reset()
            sm.current = "config"

    def reset(self):
        self.player_name.text = ""
        self.role.text = ""

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

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