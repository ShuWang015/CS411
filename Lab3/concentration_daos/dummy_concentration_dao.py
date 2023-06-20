from __future__ import annotations

from typing import List
from . import ConcentrationDao as Dao


class DummyConcentrationDao(Dao):
    """Concentration DAO for no database.

    """

    def __init__(self) -> None:
        """Initialize DummyConcentrationDao.

        """
        super().__init__()

        self._cards = None
        self._state = None
        self._matched = None

    @property
    def cards(self) -> List[str]:
        """The state.

        """
        # TODO: Implement. See part 1, dummy DAO
        return self._cards

    @state.setter
    def cards(self, cards) -> None:
        """The state.

        """
        # TODO: Implement. See part 1, dummy DAO
        self._cards = cards

    @property
    def state(self) -> List[str]:
        """The state.

        """
        # TODO: Implement. See part 1, dummy DAO
        return self._state

    @state.setter
    def state(self, state) -> None:
        """The state.

        """
        # TODO: Implement. See part 1, dummy DAO
        self._state = state

    @property
    def matched(self) -> list[str]:
        """The matched.

        """
        # TODO: Implement. See part 1, dummy DAO
        return self._matched

    @matched.setter
    def matched(self, matched: List[bool]) -> None:
        """The matched.

        """
        # TODO: Implement. See part 1, dummy DAO
        self._matched = matched
