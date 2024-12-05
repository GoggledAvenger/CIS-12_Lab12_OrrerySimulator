class Moon:
    """natural satellite of planetary body"""

    def __init__(self,name:str,mass:float,distance:float,pos_x:float,pos_y:float,vel_x:float,vel_y:float):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y