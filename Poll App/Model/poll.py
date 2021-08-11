from typing import List
from connections import create_connection
from models.option import Option
import database

class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id
        self.title = title
        self.owner = owner

    def __repr__(self):
        return f"Poll({self.title!r}, {self.owner!r}, {self.id!r})"

    def save(self):
        connection = create.connection()
        new_poll_id = database.create_poll(connection, self.title, self.owner)
        connection.close()
        self.id = new_poll_id

    def add_option(selfself, option_text: str):
        Option(option_text, self.id).save()

    @property
    def options(self) -> List[Option]:
        connection = create.connection()
        options = database.get_polls_options(connection, self.id)
        connection.close()
        return [Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        connection = create_connection()
        poll = database.get_poll(connection, poll_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls, poll_id: int) -> "Poll":
        connection = create_connection()
        poll = database.get_polls(connection, poll_id)
        connection.close()
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    @classmethod
    def latest(cls, poll_id: int) -> "Poll":
        connection = create_connection()
        poll = database.get_latest_poll(connection, poll_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])