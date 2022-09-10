from Constants_file import *
from Objects import Sphere
from Scene import scene
from TraceRay import TraceRay
from Canvas_to_viewport import canvas_to_viewport
import PIL
import numpy
from Light import Light
from Vector_classes import vector

objects = [
    Sphere(
        (0, -1, 3),
        1,
        red

    ),
    Sphere(
        (2,0,4),
        1,
        (0,0,255)

    ),




    Sphere(
        (-2,0,4),
        1,
        (0,255,0)
    ),
    Sphere((0,-5001,0), 5000, (255,255,0))

]
Light_sources = [
    Light("point", 1, vector(0,0, 0)),
    Light("ambient",0.2),
    Light("directional", 0.5, vector(1,4,4))
]

Canvas_width = 400
Canvas_height = 400
projection_plane_d = 1
Viewport_height, Viewport_width = 1, 1
"""
the distance between the origin and the viewpoint
which is a plane at z=d
"""
GP = scene(objects, Canvas_width, Canvas_height, Light_sources)
for x in range(int(-Canvas_width / 2), int((Canvas_width / 2) + 1)):
    for y in range(int(-Canvas_height / 2), int((Canvas_height / 2) + 1)):
        D = canvas_to_viewport(
            x,
            y,
            Viewport_width,
            Viewport_height,
            Canvas_width,
            Canvas_height,
            projection_plane_d

        )

        clr = TraceRay(ORIGIN, D, 1, infinity, GP)
        # if clr != colour(0,0,0): print(clr)
        GP.image.putpixel(x, y, clr)
picture = PIL.Image.fromarray(numpy.uint8(GP.image.pixels))





picture.save("output_picture.jpg")

# tempscene = numpy.zeros((100,100,3))
# for x in range(50):
#     for y in range(10):
#         # new_x, new_y = tempscene.image.cartesian_to_computer(x,y)
#         tempscene[y, x] = (255,0,0)
# picture = PIL.Image.fromarray(numpy.uint8(tempscene))
# picture.show()

def computer_to_cartesian(x,y):
    new_x =  -Canvas_width/2 + x
    new_y = Canvas_height/2 - y
    return new_x, new_y
