class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __repr__(self):
        return f"({self.__x}, {self.__y})"
