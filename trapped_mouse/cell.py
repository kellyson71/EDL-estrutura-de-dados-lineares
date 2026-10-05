class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outra):
        if not isinstance(outra, Cell):
            return False
        return self.x == outra.x and self.y == outra.y
