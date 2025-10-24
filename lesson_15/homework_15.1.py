class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __str__(self):
        return f'Romb side: {self.side_a}, \nangle_a: {self.angle_a}, \nabgle_b: {180 - self.angle_a}'

    def __setattr__(self, name, value):
        if name == "side_a":
            if type(value) not in (int, float) and value <= 0:
                raise ValueError("Incorrect value for side_a")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if type(name) not in (int, float) and not (0 < value < 180):
                raise ValueError("Invalid value for angle_a")
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)
        elif name == "angle_b":
            raise AttributeError("Not possible to set angle_b")
        else:
            raise AttributeError("Other parameters are not possible")


romb = Romb(4, 30)
print(romb.side_a, romb.angle_a, romb.angle_b)
print(romb)