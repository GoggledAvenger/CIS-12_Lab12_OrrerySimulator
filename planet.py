class Planet:
    """spherical heavenly body with relatively clear orbit"""

    def __init__(self,name:str,mass:float,distance:float,position_x:float,position_y:float,velocity_x:float,velocity_y:float):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def get_mass(self,mass:float):
        pass

    def get_distance(self,distance:float):
        pass

    def get_x_pos(self,x_p:float):
        pass

    def get_y_pos(self,y_p:float):
        pass

    def get_x_vel(self,x_v:float):
        pass

    def get_y_vel(self,y_v:float):
        pass

    def set_x_vel(self, new_x_vel:float):
        pass

    def set_y_vel(self, new_y_vel:float):
        pass

    def move_to(self, new_x:float, new_y:float):
        pass

    def __str__(self):
        return f''
