
import kivy
from kivy.uix.button import Button

import os
import enum
from random import shuffle


# Dims 500 x 726, ratio 1.452
@enum.unique
class Cards(str, enum.Enum):
    """Contains names for each playing card
    """
    CLUB_1 = "ace_of_clubs.png"
    DIAMOND_1 = "ace_of_diamonds.png"
    HEART_1 = "ace_of_hearts.png"
    SPADE_1 = "ace_of_spades.png"
    CLUB_2 = "2_of_clubs.png"
    DIAMOND_2 = "2_of_diamonds.png"
    HEART_2 = "2_of_hearts.png"
    SPADE_2 = "2_of_spades.png"
    CLUB_3 = "3_of_clubs.png"
    DIAMOND_3 = "3_of_diamonds.png"
    HEART_3 = "3_of_hearts.png"
    SPADE_3 = "3_of_spades.png"
    CLUB_4 = "4_of_clubs.png"
    DIAMOND_4 = "4_of_diamonds.png"
    HEART_4 = "4_of_hearts.png"
    SPADE_4 = "4_of_spades.png"
    CLUB_5 = "5_of_clubs.png"
    DIAMOND_5 = "5_of_diamonds.png"
    HEART_5 = "5_of_hearts.png"
    SPADE_5 = "5_of_spades.png"
    CLUB_6 = "6_of_clubs.png"
    DIAMOND_6 = "6_of_diamonds.png"
    HEART_6 = "6_of_hearts.png"
    SPADE_6 = "6_of_spades.png"
    CLUB_7 = "7_of_clubs.png"
    DIAMOND_7 = "7_of_diamonds.png"
    HEART_7 = "7_of_hearts.png"
    SPADE_7 = "7_of_spades.png"
    CLUB_8 = "8_of_clubs.png"
    DIAMOND_8 = "8_of_diamonds.png"
    HEART_8 = "8_of_hearts.png"
    SPADE_8 = "8_of_spades.png"
    CLUB_9 = "9_of_clubs.png"
    DIAMOND_9 = "9_of_diamonds.png"
    HEART_9 = "9_of_hearts.png"
    SPADE_9 = "9_of_spades.png"
    CLUB_10 = "10_of_clubs.png"
    DIAMOND_10 = "10_of_diamonds.png"
    HEART_10 = "10_of_hearts.png"
    SPADE_10 = "10_of_spades.png"
    CLUB_11 = "jack_of_clubs.png"
    DIAMOND_11 ="jack_of_diamonds.png"
    HEART_11 = "jack_of_hearts.png"
    SPADE_11 = "jack_of_spades.png"
    CLUB_12 ="queen_of_clubs.png"
    DIAMOND_12 ="queen_of_diamonds.png"
    HEART_12 = "queen_of_hearts.png"
    SPADE_12 = "queen_of_spades.png"
    CLUB_13 = "king_of_clubs.png"
    DIAMOND_13 = "king_of_diamonds.png"
    HEART_13 = "king_of_hearts.png"
    SPADE_13 = "king_of_spades.png"

    BLACK_JOKER = "black_joker.png"

    FACE_DOWN = "facedown.png"


class PlayingCard(Button):
    card: Cards
    def __init__(self, img_name, *args, width=200, on_press=None, **kwargs):
        self.card = Cards(img_name)
        # super().__init__(*args, width=width, height=width*1.452, padding=(20, 20), on_press=on_press, **kwargs)
        super().__init__(*args, background_normal=os.path.join("cards", img_name), width=width, height=width*1.452, padding=(20, 20), on_press=on_press, **kwargs)


class CardPicker():
    """Random card picker.

    Picks card from deck and remembers which ones have been used.
    """
    def __init__(self):
        cards = list(Cards)
        cards.remove(Cards.FACE_DOWN)
        shuffle(cards)
        self._cards = cards
        self._current_cards = self._cards.copy()
    def __iter__(self):
        for card in self._cards:
            yield self._current_cards.pop()
    
    def cards_left():
        """How many cards left.

        Returns:
            int: len of remaining deck
        """
        return len(self._current_cards)
    
    def restart():
        """Restart and set deck to contain all cards.
        """
        self._current_cards = self._cards



if __name__ == "__main__":
    for c in CardPicker():
        print(c)
