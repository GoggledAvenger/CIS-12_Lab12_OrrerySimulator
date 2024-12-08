class Sun:
    """the star which Earth orbits"""

    def __init__(self,name:str,radius:float,mass:float,position_x:float,position_y:float,appearance:str):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.position_x = position_x
        self.position_y = position_y
        self.appearance = appearance

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.position_x

    def get_y_pos(self):
        return self.position_y

    def __str__(self):
        return f'name: {self.name}, radius: {self.radius}, mass: {self.mass}, position: {self.position_x},{self.position_y}'