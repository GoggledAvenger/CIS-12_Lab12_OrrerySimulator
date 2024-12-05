class Sun:
    """the star which Earth orbits"""

    def __init__(self,name:str,mass:float,position_x:float,position_y:float):
        self.name = name
        self.mass = mass
        self.position_x = position_x
        self.position_y = position_y

    def get_mass(self):
        pass

    def get_x_pos(self,x:float):
        pass

    def get_y_pos(self,y:float):
        pass

    def __str__(self):
        return f''