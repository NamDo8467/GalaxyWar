from collections import deque
from src.Brick import Brick
from src.Colors import colors
from random import randrange


class Wall:
    __color_list = list(colors.values())
    __number_of_colors = 6
    __distance_between_layer = -10.5

    def __init__(self):
        self.queue = deque()
        for i in range(0, 440, 20):  # range(start=0, stop=440 (not included), step=20)
            brick = Brick(i, 0, self.__color_list[randrange(0, self.__number_of_colors)])
            self.queue.append(brick)

    def addLayerOfBricks(self):
        for brick in self.queue:
            if brick.y == 410 or brick.y > 410:  # 410 is the Y-coordinate that hits the spaceship which will make the game stops
                return
            brick.y += 0.5

        for i in range(0, 440, 20):  # range(start=0, stop=440 (not included), step=20)
            brick = Brick(i, self.__distance_between_layer,
                          self.__color_list[randrange(0, self.__number_of_colors - 1)])
            self.queue.append(brick)
        self.__distance_between_layer -= 10.5

    def removeBrick(self, brick):
        self.queue.remove(brick)


