class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.

    Methods:
        __init__(self, size): Initializes a square with the given size.

    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        Parameters:
            size (int): The size of the square.

        """
        self.__size = size  # Private instance attribute

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size
