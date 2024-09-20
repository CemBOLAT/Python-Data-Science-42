from S1E9 import Character


class Baratheon(Character):
    """Baratheon character"""
    def __init__(self, first_name, is_alive=True):
        """Baratheon Characters Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return the string representation of the object"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Return the string representation of the object"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    """Lannister character"""
    def __init__(self, first_name, is_alive=True):
        """Lannister Characters Constructor """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister character"""
        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """Return the string representation of the object"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Return the string representation of the object"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
