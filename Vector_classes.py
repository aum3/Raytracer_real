from math import sqrt
class vector:
    # def __init__(self, values):
    #     x,y,z = values
    #     self.x = x
    #     self.y = y
    #     self.z = z
    def __init__(self, x,y=None,z=None):
        if y==None and z==None and isinstance(x,vector):
            x,y,z = x.returntuple()

        if isinstance(x,tuple):
            v1, v2, v3 = x
            x,y,z = v1,v2,v3
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"vector ({self.x}, {self.y}, {self.z})"
    def __add__(self, other):
        return vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __mul__(self, other):
        if isinstance(other, vector):
            return (self.x*other.x+self.y*other.y+self.z*other.z)
        else:
            return vector(self.x*other, self.y*other, self.z*other)
    def __sub__(self, other):
        tempvector = other*-1
        return (tempvector + self)
    def __truediv__(self, other):
        return vector(self.x/other, self.y/other, self.z/other)
    def returntuple(self):
        return (self.x, self.y, self.z)
    def magnitude(self):
        return sqrt((self.x)**2 +(self.y)**2 +(self.z)**2  )
    def normalise(self):
        modulus = self.magnitude()
        return self/(modulus)

point = vector
