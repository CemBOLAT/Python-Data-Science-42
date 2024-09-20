class calculator:
    """A simple calculator class"""

    def __init__(self, list) -> None:
        """Constructor"""
        self.list = list

    def __add__(self, object) -> None:
        """
        Description: Add a number to the list
        Args:
            object: a number
        Returns:
            None
        Logic:
            Add the number to each element of the list
        """
        self.list = [x + object for x in self.list]
        print(self.list)

    def __mul__(self, object) -> None:
        """
        Description: Multiply a number to the list
        Args:
            object: a number
        Returns:
            None
        Logic:
            Multiply the number to each element of the list.
        """
        self.list = [x * object for x in self.list]
        print(self.list)

    def __sub__(self, object) -> None:
        """
        Description: Subtract a number to the list
        Args:
            object: a number
        Returns:
            None
        Logic:
            Subtract the number to each element of the list.
        """
        self.list = [x - object for x in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:
        """
        Description: Divide a number to the list
        Args:
            object: a number
        Returns:
            None
        Logic:
            Divide the number to each element of the list.
        """
        try:
            self.list = [x / object for x in self.list]
            print(self.list)
        except ZeroDivisionError:
            pass
