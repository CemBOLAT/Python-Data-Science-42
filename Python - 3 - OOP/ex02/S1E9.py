from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character Class """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character Constructor """
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Stark character """
    def __init__(self, first_name, is_alive=True):
        """Stark Characters Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character """
        self.is_alive = False
