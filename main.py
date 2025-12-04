from simunlation import Simulation
from solarsystem import SolarSystem
from sun import Sun
from planet import Planet

def main():
    solar_sys = SolarSystem()
    solar_sys.add_sun(Sun(name="mysun", radius=5, mass=100, temp=1000, x = 7.0, y = 0.0))
    solar_sys.add_planet(Planet(name="ohno", radius=22.0, mass=0.33, x = 100, y = 0.0, vel_x = 100, vel_y = 200, distance = 3000))
    sim = Simulation(solar_sys, 500, 500, 100)
    solar_sys.show_planets()
    sim.run()

if __name__ == '__main__':
    main()