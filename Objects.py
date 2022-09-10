from Constants_file import infinity
from Vector_classes import *
from Colour_class import colour as clr
from math import sqrt


class Sphere:
    def __init__(self, center, radius, colour):
        self.center, self.radius, self.colour = point(center), (radius), clr(colour)

    def intersect_with_ray(self, O, D):
        """

        :param O: Origin's coordinates
        :param D: the vector of the ray moving from the origin to V,
        the specific viewpoint coordinate we want to check
        :return: The t-values (t1,t2) for which the ray
        and sphere intersect, if any

        """
        if not (isinstance(O, point)):
            O = point(O)
        if not (isinstance(D, vector)):
            D = vector(D)
        CO = (O - self.center)

        # vector from center of the circle to the origin
        # change the variable name using find and replace
        a = D * D
        b = 2 * (CO * D)
        c = CO * CO - (self.radius) ** 2
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return infinity, infinity
        t1 = (-b + sqrt(discriminant)) / 2 * a
        t2 = (-b - sqrt(discriminant)) / 2 * a
        return t1, t2


class ray:
    def __init__(self, p1, p2, origin):
        """

        :param p1: first point it goes through
        :param p2: second point it goes through

        D vector is the vector going from one point
        to another. I.e the direction ya dunno.
        Require that p2 > p1
        """
        assert p2 > p1

        if not isinstance(p1, point):
            p1 = point(p1)
        if not isinstance(p2, point):
            p2 = point(p2)
        if not isinstance(origin, point):
            origin = point(origin)
        self.D_vector = p2 - p1
        self.origin = origin

    def coord_from_t(self, t):
        # print(f"doing {t} multiplied by {self.D_vector}")
        new_point = self.D_vector * t
        new_point += self.origin

        return new_point



