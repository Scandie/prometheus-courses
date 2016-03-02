import math


class Sphere(object):

    def __init__(self, radius=1, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4*math.pi*(self.radius**3))/3

    def get_square(self):
        return 4*math.pi*(self.radius**2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        flag = False
        if (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2 < self.radius**2:
            flag = True
        return flag



test = Sphere()
test.set_center(0.5, 1, 0)
test.set_radius(1.1)
print test.get_radius()
print test.get_center()
print test.get_volume()
print test.is_point_inside(0, 0.99, 0)




