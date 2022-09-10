from Vector_classes import vector
from Vector_classes import point


class Light:
    def __init__(self, type, intensity, directionvector_or_position=None):
        """

        :param type: strings: "ambient" or "point"
        or "directional"
        :param intensity: real number between 0 and 1
        :param directionvector_or_position: 3d point in space
        if type is point. Otherwise direction vector if
        type is directional
        """
        assert type in ['ambient', 'point', 'directional']
        self.type, self.intensity, = type, intensity
        self.position, self.direction_vector = None, None
        if self.type == "point":
            self.position = point(directionvector_or_position)
        elif self.type == "directional":
            self.direction_vector = vector(directionvector_or_position)



