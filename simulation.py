from solar_system import SolarSystem

class Simulation:
    """digital orrery"""

    orrery = SolarSystem()

    def __init__(self,name,width:int,height:int,num_periods:int):
        self.name = name
        self.width = width
        self.height = height
        self.num_periods = num_periods

    def run(self):
        pass