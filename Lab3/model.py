from __future__ import annotations

import random
import requests
from typing import List, Optional
from concentration_daos import DummyConcentrationDao as DummyDao
from concentration_daos import ConcentrationDao as ConDao

class ConcentrationModel:
    """Model for concentration game.

    """

    def __init__(self, dao_identifier: Optional[str] = None) -> None:
        """Initialize ConcentrationModel.

        Parameters
        ----------
        dao_identifier : str (default=`None`)
            "redis" for Redis, "sqlite" for SQLite.

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
        cards = self.shuffle(cards=cards)
        
        if dao_identifier = None:
            self._dao = DummyDao()
        elif dao_identifier='sqlite':
            self._dao = ConDao()

        self._dao.cards = cards
        self._dao.state = ['down'] * 52
        self._dao.matched = [False] * 52

    def shuffle(self, cards: List[str]) -> List[str]:
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
        # TODO: Implement, see part 2, add dummy dao to model
        r = requests.get('https://www.random.org/integers/?num=1&min=1&max=5&col=1&base=10&format=plain&rnd=new')
        o = r.content[0]

        random.seed(o)
        random.shuffle(cards)
        return cards

    @property
    def cards(self) -> List[str]:
        """The cards.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        return self._dao.cards

    @cards.setter
    def cards(self, cards: List[str]) -> None:
        """The cards.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        self._dao.cards = cards

    @property
    def state(self) -> List[str]:
        """The state.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        return self._dao.state

    @state.setter
    def state(self, state: List[str]) -> None:
        """The state.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        self._dao.state = state

    @property
    def matched(self) -> List[bool]:
        """The matched.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        return self._dao.matched

    @matched.setter
    def matched(self, matched: List[bool]) -> None:
        """The matched.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        self._dao.matched = matched

    def game_over(self) -> bool:
        """Checks if the game is over.

        Returns
        -------
        status : bool
            `True` if the game is over. `False` otherwise.

        """
        # TODO: Implement, see part 2, add dummy dao to model
        if False in self._dao.matched:
            return False
        return True
