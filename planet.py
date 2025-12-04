class Planet:
    def __init__(
        self,
        name: str,
        radius: float,
        mass: float,
        distance: float,
        x: float,
        y: float,
        vel_x: float = 0.0,
        vel_y: float = 0.0
    ):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
        self._x = x
        self._y = y
        self._vel_x = vel_x
        self._vel_y = vel_y

    # Getters
    def get_mass(self) -> float:
        return self._mass

    def get_distance(self) -> float:
        return self._distance

    def get_x_pos(self) -> float:
        return self._x

    def get_y_pos(self) -> float:
        return self._y

    def get_x_vel(self) -> float:
        return self._vel_x

    def get_y_vel(self) -> float:
        return self._vel_y

    # Setters
    def set_x_vel(self, new_x_vel: float):
        self._vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self._vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self._x = new_x
        self._y = new_y

    def __str__(self) -> str:
        return (f"Planet(name={self._name}, mass={self._mass}, "
                f"pos=({self._x}, {self._y}), vel=({self._vel_x}, {self._vel_y}))")