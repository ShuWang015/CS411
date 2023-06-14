from __future__ import annotations
import random


class ConcentrationModel:
    """Model for concentration game.

    """

    def __init__(self) -> None:
        """Initialize ConcentrationModel.

        """
        values = [
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'j',
            'q',
            'k',
            'a'
        ]
        suits = [
            'c',
            'd',
            'h',
            's'
        ]

        cards = []
        for value in values:
            for suit in suits:
                cards.append(value + suit)
        random.shuffle(cards)

        self._cards = cards
        self._state = ['down'] * 52
        self._matched = [False] * 52

    @property
    def cards(self):
        """The cards.

        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """The cards.

        """
        self._cards = cards

    @property
    def state(self):
        """The state.

        """
        return self._state

    @state.setter
    def state(self, state):
        """The state.

        """
        self._state = state

    @property
    def matched(self):
        """The matched.

        """
        return self._matched

    @matched.setter
    def matched(self, matched):
        """The matched.

        """
        self._matched = matched

    def game_over(self) -> bool:
        """Checks if the game is over.

        Returns
        -------
        status : bool
            `True` if the game is over. `False` otherwise.

        """
        # TODO: Implement. See Part 1: Game over.

        if False in self.matched:
            return False
        return True
