from __future__ import annotations

from typing import List
import sqlite3
from . import ConcentrationDao as Dao

class SQLiteConcentrationDao(Dao):
    """Concentration DAO for SQLite.

    """

    def __init__(self) -> None:
        """Initialize SQLiteConcentrationDao.

        Parameters
        ----------
        database : str (default=`concentration.db`)
            The database name.

        """
        super().__init__()

        self._logger.info("Connecting to SQLite.")

        # Create connection to SQLite
        self._connection = sqlite3.connect(database='concentration.db', check_same_thread=False)

        # Create tables for cards and matched
        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS cards(item)")
        cursor.execute("CREATE TABLE IF NOT EXISTS matched(item)")
        cursor.close()

    @property
    def cards(self) -> List[str]:
        """The cards.

        """
        self._logger.info("Getting cards from SQLite.")

        cursor = self._connection.cursor()
        # Select all rows from cards table
        cursor.execute("SELECT item FROM cards")
        rows = cursor.fetchall()
        # first entry in each row is the card string
        cards = [row[0] for row in rows]
        cursor.close()
        return cards

    @cards.setter
    def cards(self, cards: List[str]) -> None:
        """The cards.

        """
        self._logger.info("Setting cards in SQLite.")
        self._logger.debug(cards)
        cursor = self._connection.cursor()
        # Delete all rows from cards table
        cursor.execute("DELETE FROM cards")
        # Add each card as new row in cards table
        for item in cards:
            cursor.execute("INSERT INTO cards(item) VALUES(?)", (item,))
        self._connection.commit()
        cursor.close()

    @property
    def matched(self) -> list[bool]:
        """The matched.

        """
        # TODO: Implement. See part 3, finish sqlite dao.
        self._logger.info("Getting matched from SQLite.")

        cursor = self._connection.cursor()
        # Select all rows from cards table
        cursor.execute("SELECT item FROM matched")
        rows = cursor.fetchall()
        # first entry in each row is the card string
        matched = [row[0] for row in rows]
        for i in range(len(matched)):
            if matched[i]:
                matched[i] = True
            else:
                matched[i] = False
        cursor.close()
        return matched

    @matched.setter
    def matched(self, matched: List[bool]) -> None:
        """The matched.

        """
        # TODO: Implement. See part 3, finish sqlite dao.
        self._logger.info("Setting matched in SQLite.")
        self._logger.debug(matched)
        cursor = self._connection.cursor()
        # Delete all rows from cards table
        cursor.execute("DELETE FROM matched")
        # Add each card as new row in cards table
        for item in matched:
            cursor.execute("INSERT INTO matched(item) VALUES(?)", (item,))
        self._connection.commit()
        cursor.close()
