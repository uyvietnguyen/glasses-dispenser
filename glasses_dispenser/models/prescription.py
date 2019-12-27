from _decimal import Decimal


class Prescription:
    def __init__(self, sphere, cylinder, axis, add):
        sphere = '{:.2f}'.format(round(sphere, 2))
        cylinder = '{:.2f}'.format(round(cylinder, 2))

        self.sphere = sphere
        self.cylinder = cylinder
        self.axis = axis
        self.add = add
        self.dispensed = False
