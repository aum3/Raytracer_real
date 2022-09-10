from Constants_file import *
from Objects import Sphere
from Vector_classes import vector
from Compute_lighting_funcion import ComputeLighting

def TraceRay(origin, D_vector, t_min, t_max, scene):
    """

    :param origin: coordinates of origin
    :param D_vector: vector of direction of ray
    :param t_min: minimum t-value we want to find intersectins within
    :param t_max: max t-value
    :param scene: the container of objects and other things.
    :return: returns the colour of the sphere at the nearest
    intersection inside the requested range of t. Ie , given a
    direction vector and an origin and a specific sphere,
    we find the nearest intersection with a sphere. This code
    defo gonna haffi be appended
    """
    closest_t = infinity
    closest_sphere = None
    for sphere in scene.spheres:
        t1, t2 = sphere.intersect_with_ray(origin, D_vector)
        if t_min<=t1<=t_max and t1<closest_t:
            closest_t = t1
            closest_sphere = sphere
        if t_min<=t2<=t_max and t2<closest_t:
            closest_t = t2
            closest_sphere = sphere
            """
            basically, once weve found the t-values at which
            the sphere and ray intersect (look at the book for
            the meaning of t), then we find which t_value is smaller 
            as we want the intersection point that is closer to the
            camera as the other one wouldnt be visible in the camera. 
            The reason for the closest_sphere is because one of the 
            t_values could be invalid. 
            """
    if closest_sphere == None:
        return BACKGROUND_COLOUR
    else:
        point = origin + D_vector*closest_t #confirmed correct
        N = point - closest_sphere.center#confirmed correct
        N = N.normalise()#confirmed correct
        return closest_sphere.colour*ComputeLighting(point, N, scene)





