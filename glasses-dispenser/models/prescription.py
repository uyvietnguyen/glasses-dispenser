def __init__(self, sphere, cylinder, axis, add):
    sphere = round(sphere, 2)
    cylinder = round(cylinder, 2)

    self.sphere = sphere
    self.cylinder = cylinder
    self.axis = axis
    self.add = add
    self.dispensed = False
