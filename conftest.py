import pytest


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self) -> None:
        self.name = "Artur"
        self.second_name = "Leleiko"

    def remove(self) -> None:
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()
