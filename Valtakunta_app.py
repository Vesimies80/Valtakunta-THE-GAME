import kivy
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.label import MDLabel

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from cards import CardPicker, PlayingCard, Cards

import enum
from typing import List

from dataclasses import dataclass

roles = ["kansalainen", "kurtesaani", "orja", "aatelinen", "hallitsija"]

class InValuesMeta(enum.EnumMeta): 
    def __contains__(cls, item): 
        return item in [v.value for v in cls.__members__.values()] 


class Roles(str, enum.Enum, metaclass=InValuesMeta):
    KANSALAINEN = "kansalainen"
    KURTESAANI = "kurtesaani"
    ORJA = "orja"
    AATELINEN = "aatelinen"
    HALLITSIJA = "hallitsija"
    
@dataclass
class Player:
    name: str
    role: Roles


class ValtakuntaApp(MDApp):
    players: List[Player]
    def __init__(self):
        super().__init__()
        self.players = []

    def build(self):
        return sm

valtakunta = ValtakuntaApp()

class RolesIconListItem(OneLineIconListItem):
    """Roles icon list
    """
    icon = StringProperty()
class ConfigWindow(Screen):
    

    player_name = ObjectProperty(None)
    role = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "viewclass": "RolesIconListItem",
                "icon": "git",
                "text": f"{role}",
                "height": dp(56),
                "on_release": lambda x=f"{role}": self.set_item(x),
            } for role in sorted(Roles)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.role,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.bind()
    
    def submitbtn(self):
        if self.player_name.text != "" and self.role.text != "":
            if self.ids.role.text.lower() not in Roles:
                content=Button(text="The inputted role is invalid try: \n" + ", ".join(role for role in Roles))
                pop = Popup(title='Invalid Role',content=content, auto_dismiss=False)
                content.bind(on_press=pop.dismiss)
                pop.open()

            else:
                valtakunta.get_running_app().players.append(Player(self.player_name.text, Roles(self.ids.role.text)))
                self.reset()
    
    def set_item(self, text_item):
        self.ids.role.text = text_item
        self.menu.dismiss()

    def start_game(self):
        if len(valtakunta.get_running_app().players) == 0:
            content=Button(text="No players inputted")
            pop = Popup(title='No players',content=content, auto_dismiss=False)
            content.bind(on_press=pop.dismiss)
            pop.open()
        else:
            self.reset()
            print(valtakunta.get_running_app().players)
            sm.current = "MainWindow"

    def reset(self):
        self.player_name.text = ""
        self.ids.role.text = "Player role"

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.card = None
        self.infolbl = None
        self.card_picker = CardPicker()
        self.card_picker_iter = iter(self.card_picker)
        self.replace_card(Cards.FACE_DOWN)
        

    def new_card(self, card):
        new_card = next(self.card_picker_iter)
        print(new_card)
        self.replace_card(new_card)

    def replace_card(self, card: Cards):
        if self.card:
            self.ids.floatlayout.remove_widget(self.card)
        # self.card = PlayingCard(card, pos_hint={"x": 0.1, "top": 0.4})
        self.card = PlayingCard(card, on_press=self.new_card, pos_hint={"x": 0.1}, size_hint=(2/5, 1.452*2/5))
        # self.card = Button(text="foo", pos_hint={"x":0.4, "top":0.9})
        self.ids.floatlayout.add_widget(self.card)
    
    def on_enter(self):
        self.ids.foo.text = valtakunta.get_running_app().players[0].name
    
    def infolbl(self,text):
        if self.infolbl:
            self.ids.floatlayout.remove_widget(self.infolbl)
        self.infolbl = MDLabel(text=text, pos_hint={"x":0.9},size_hint=(2/5,1.452*2/5))
        self.ids.floatlayout.add_widget(self.infolbl)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("valtakunta.kv")
sm = WindowManager()
screens = [ConfigWindow(name="config"), MainWindow(name="MainWindow")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "config"


if __name__ == "__main__":
    valtakunta.run()