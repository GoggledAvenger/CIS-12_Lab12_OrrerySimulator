class Planet:
    """spherical heavenly body with relatively clear orbit"""

    def __init__(self,
                 name:str,
                 radius:float,
                 mass:float,
                 distance:float,
                 position_x:float,
                 position_y:float,
                 velocity_x:float,
                 velocity_y:float,
                 appearance:str
                 ):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.appearance = appearance

    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance

    def get_x_pos(self):
        return self.position_x

    def get_y_pos(self):
        return self.position_y

    def get_x_vel(self):
        return self.velocity_x

    def get_y_vel(self):
        return self.velocity_y

    def set_x_vel(self, new_x_vel:float):
        pass

    def set_y_vel(self, new_y_vel:float):
        pass

    def move_to(self, new_x:float, new_y:float):
        vel_new_x = new_x + self.velocity_x
        vel_new_y = new_y + self.velocity_y
        return vel_new_x, vel_new_y

    def __str__(self):
        return (f'name: {self.name}, radius: {self.radius}, mass: {self.mass}, distance: {self.distance}, '
                f'position: {self.position_x},{self.position_y}, velocity: {self.velocity_x},{self.velocity_y}, '
                f'appearance: {self.appearance}')