class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    # We override the __setattr__ method to control the setting of attributes
    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("The side value must be greater than 0.")
            super().__setattr__(name, value)
        elif name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("The angle must be in the range from 0 to 180 degrees.")
            super().__setattr__(name, value)
            super().__setattr__('angle_b', 180 - value)
        else:
            super().__setattr__(name, value)

    # A method for deriving information about a rhombus
    def get_info(self):
        return f"Side a: {self.side_a}, Angle α: {self.angle_a}, Angle β: {self.angle_b}"


try:
    rhombus = Rhombus(5, 60)  #
    print(rhombus.get_info())  #
except ValueError as e:
    print(e)



