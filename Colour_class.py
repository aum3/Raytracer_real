from Vector_classes import vector
class colour:
    def __init__(self,red, green = 0, blue = 0):

        if isinstance(red, tuple):
            temptuple = red
            red, green, blue = temptuple
        self.red = red
        self.green = green
        self.blue = blue
        if self.red>255 : self.red = 255
        if self.red<0 : self.red = 0
        if self.green>255 : self.green = 255
        if self.green<0 : self.green = 0
        if self.blue>255 : self.blue = 255
        if self.blue<0 : self.blue = 0
    def __str__(self):
        return f"colour: ( {self.red}, {self.green}, {self.blue} )"
    def __add__(self, other):
        return colour(self.red+ other.red, self.green+other.green, self.blue +other.blue)
    def returnvector(self):
        return vector(self.red, self.green, self.blue)
    def returntuple(self):
        return (self.red, self.green, self.blue)
    def __mul__(self, other):
        return colour(self.red*other, self.green*other, self.blue*other)

