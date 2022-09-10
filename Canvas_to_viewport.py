from Vector_classes import point
def canvas_to_viewport(x,y,Vw,Vh,Cw,Ch,d):
    """

    :param d: distance of the viewport from the
    camera. The viewport is on the z-value of d
    :param x: x coordinate on the canvas
    :param y: y coordinate on the canvas
    :param Vw: width of the viewport, the
    "window" in 3d space that we are looking into
    :param Vh: height of the viewport
    :param Cw: canvas width
    :param Ch: canvas height
    :return: the 3d coordinate of the intersection
    point of the viewpoint
    """
    tempx = x*(Vw/Cw)
    tempy = y*(Vh/Ch)
    return point(tempx, tempy, d)