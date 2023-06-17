from __future__ import annotations

import random
import requests
from typing import List


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
        cards = self._shuffle(cards=cards)

        self._cards = cards
        self._state = ['down'] * 52
        self._matched = [False] * 52

    def _shuffle(self, cards: List[str]) -> List[str]:
        """Shuffle the cards.

        The Random.org API is called to access a random seed for shuffling.

        Parameters
        ----------
        cards : List[str]
            The unshuffled cards.

        Returns
        -------
        cards : List[str]
            The shuffled cards.

        """
        # TODO: Part 2, Implementation.
        r = requests.get('https://www.random.org/integers/?num=1&min=1&max=5&col=1&base=10&format=plain&rnd=new')
        seed = r.content[0]
        random.seed(seed)
        random.shuffle(cards)
        return cards

    @property
    def cards(self) -> List[str]:
        """The cards.

        """
        return self._cards

    @cards.setter
    def cards(self, cards: List[str]) -> None:
        """The cards.

        """
        self._cards = cards

    @property
    def state(self) -> List[str]:
        """The state.

        """
        return self._state

    @state.setter
    def state(self, state: List[str]) -> None:
        """The state.

        """
        self._state = state

    @property
    def matched(self) -> List[bool]:
        """The matched.

        """
        return self._matched

    @matched.setter
    def matched(self, matched: List[bool]) -> None:
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
        return all(self._matched)
