class Brick:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.__height = 10
        self.__width = 20

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width
