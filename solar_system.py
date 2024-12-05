import math
from planet import Planet
from sun import Sun
from gravity import Gravity

class SolarSystem:
    """gravitationally bound heavenly bodies to and including the sun"""

    the_sun = Sun('SOL',1.9891,0,0)
    planets = []

    def add_planet(self,new_planet:Planet):
        pass

    def add_sun(self,the_sun:Sun):
        pass

    def show_planets(self):
        pass

    def move_planets(self):
        dt = .001  # Constant time interval for each solar system iteration.

        for planet in self.planets:
            # Move the distance covered in the interval dt
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            # After move we need to calculate the new distance from the sun using the distance formula.
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x**2 + dist_y**2)

            # Let's calculate our new acceleration so we can set our new velocity
            acc_x = Gravity.G * self.the_sun.get_mass()*dist_x/new_distance**3
            acc_y = Gravity.G * self.the_sun.get_mass()*dist_y/new_distance**3

            # Now let's calculate the new x and y velocities and update them for the planet
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)