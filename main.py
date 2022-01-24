
from kivy.app import App


from cards import PlayingCard, CardPicker, Cards


class MyApp(App):
    def build(self):
        return PlayingCard(Cards.FACE_DOWN, on_press=lambda x: print("foo", x, x.card))


if __name__ == "__main__":
    MyApp().run()
    # for c in CardPicker():
    #     print(c)
