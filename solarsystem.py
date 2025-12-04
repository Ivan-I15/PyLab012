from sun import Sun
from planet import Planet
from UniversalGravity import UniversalGravity
import math


class SolarSystem:
    def __init__(self):
        self._the_sun: Sun | None = None
        self._planets: list[Planet] = []

    def add_sun(self, the_sun: Sun):
        self._the_sun = the_sun

    def add_planet(self, new_planet: Planet):
        self._planets.append(new_planet)

    def show_planets(self):
        for p in self._planets:
            print(p)

    def move_planets(self, dt: float = 1.0):
        """Move planets using Newtonian gravity toward the Sun."""
        if not self._the_sun:
            raise ValueError("No Sun in solar system")

        for planet in self._planets:
            dx = self._the_sun.get_x_pos() - planet.get_x_pos()
            dy = self._the_sun.get_y_pos() - planet.get_y_pos()
            distance = math.sqrt(dx*dx + dy*dy)

            # gravitational force magnitude
            force = UniversalGravity.G * self._the_sun.get_mass() * planet.get_mass() / distance**2

            # acceleration
            ax = force * dx / (distance * planet.get_mass())
            ay = force * dy / (distance * planet.get_mass())

            # update velocity
            planet.set_x_vel(planet.get_x_vel() + ax * dt)
            planet.set_y_vel(planet.get_y_vel() + ay * dt)

            # update position
            new_x = planet.get_x_pos() + planet.get_x_vel() * dt
            new_y = planet.get_y_pos() + planet.get_y_vel() * dt
            planet.move_to(new_x, new_y)

