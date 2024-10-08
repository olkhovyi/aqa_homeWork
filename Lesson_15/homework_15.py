class Rhombus:
    def __init__(self, side_a, angle_a):
        self.setattr('side_a', side_a)
        self.setattr('angle_a', angle_a)

    def setattr(self, attr_name, value):
        if attr_name == 'side_a':
            if value <= 0:
                raise ValueError("The side value must be greater than 0.")
            self.__dict__[attr_name] = value
        elif attr_name == 'angle_a':
            if value <= 0 or value >= 180:
                raise ValueError("The angle must be greater than 0 and less than 180 degrees.")
            # Angle b is automatically calculated based on the fact that the sum of the angles must be equal to 180 degrees
            angle_b = 180 - value
            self.__dict__[attr_name] = value
            self.__dict__['angle_b'] = angle_b
        else:
            raise AttributeError(f"Unknown attribute: {attr_name}")

    def get_info(self):
        return f"Side a: {self.side_a}, Angle α: {self.angle_a}, Angle β: {self.angle_b}"


try:
    rhombus = Rhombus(3, 40)
    print(rhombus.get_info())
except ValueError as e:
    print(e)
