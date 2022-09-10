from imagation import image


class scene:
    def __init__(self, spheres, width, height, light_sources):
        self.spheres = spheres
        self.height = height
        self.width = width
        self.image = image(height, width)
        self.light_sources = light_sources

