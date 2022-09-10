from Vector_classes import vector
from Light import Light
from Scene import scene
from numpy import dot
import numpy
def ComputeLighting(Point, Normal_vector, scene):
    """

    :param Point: 3d coordinate of the point we're interested
    in finding the light intensity at
    :param Normal_vector:
    the normal vector at this point
    :param scene:
    the container for the objects within the scene
    :return:
    returns i, the light intensity of a point
    """


    assert isinstance(Point, vector) and isinstance(Normal_vector, vector)
    assert len(scene.light_sources) > 0
    i = 0.0
    for light_source in scene.light_sources:
        if light_source.type == "ambient":
            i+=light_source.intensity
        else:
            if light_source.type == "point":
                Light_vector = light_source.position - Point#Confirmed correct
            else:
                Light_vector = light_source.direction_vector

            Light_vector = Light_vector.normalise()
            # NL_dot = Normal_vector*Light_vector
            NL_dot = dot(Normal_vector.returntuple(), Light_vector.returntuple())#cc
            if NL_dot > 0:
                Light_vector_magnitude =  numpy.sqrt(dot(Light_vector.returntuple(),Light_vector.returntuple()))#cc
                i += light_source.intensity*(NL_dot/(1 * Light_vector_magnitude))
                #replaced "Normal_vector.magnitude()" above with 1
    return i


