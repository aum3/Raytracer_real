import numpy as np
from PIL import Image
import PIL
import numpy
from Colour_class import colour as clr


class image:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.pixels = np.zeros((height, width, 3))
        #i swapped height and width in the above statement
    def putpixel(self, x, y, colour):
        if not isinstance(colour, clr): colour = clr(colour)
        x,y = self.cartesian_to_computer(x,y)
        # self.pixels[y, x] = colour.returntuple() ORIGINAL
        try : self.pixels[y,x] = colour.returntuple()
        except: pass

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def cartesian_to_computer(self, x, y):
        """

        :param x: x-value in the cartesian system
        :param y: y-value in the cartesian system
        :return: the computer coordinates from the cartesian coordinates. X varies between -width/2 to width/2 and
        same for the y-value
        """
        w = self.width
        h = self.height
        assert w / 2 >= x >= -w / 2
        assert h / 2 >= y >= -h / 2
        Cx = int(x+(w/2))
        Cy = int(y+(h/2))
        Cy = w-Cy
        return Cx, Cy



