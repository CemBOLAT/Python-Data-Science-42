class calculator:
    """
    A simple calculator class
    Methods:
        dotproduct(V1: list[float], V2: list[float]) -> None:
        add_vec(V1: list[float], V2: list[float]) -> None:
        sous_vec(V1: list[float], V2: list[float]) -> None:
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Description: Calculate the dot product of two vectors
        Args:
            V1: a list of float
            V2: a list of float
        Returns:
            None
        Logic:
            Calculate the dot product of two
        """
        result = 0
        for i, j in zip(V1, V2):
            result += i * j
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Description: Add two vectors
        Args:
            V1: a list of float
            V2: a list of float
        Returns:
            None
        Logic:
            Add two vectors
        """
        result = [i + j for i, j in zip(V1, V2)]
        print(f"Add vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Description: Subtract two vectors
        Args:
            V1: a list of float
            V2: a list of float
        Returns:
            None
        Logic:
            Subtract two vectors
        """
        result = [i - j for i, j in zip(V1, V2)]
        print(f"Sous vector is: {result}")
