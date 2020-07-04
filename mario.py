"""A class representiing Super Mario"""

class SuperMario:
    """
    Class representing sumer mario and its methods
        Attributes:
            x and y (int): x,y position of mario(starting position)
            w and h (int): height and width of mario
    """

    def __init__(self, x, y, w, h):
        """constructor for mario"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.gravity = .25
        self.jump = 4
        self.speed = 0
        self.rotation = 0

    def draw(self):
        """ Draw the mario on the screen """
        

    def update(self):
        """
        update the position and method in every frame

        self.speed += self.graity

        self.y += self.speed

        """
        

