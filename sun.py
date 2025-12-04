class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: int = 0.0, y: int = 0.0):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._temp = temp
        self._x = x
        self._y = y

    # Getters
    def get_mass(self) -> float:
        return self._mass

    def get_x_pos(self) -> int:
        return self._x

    def get_y_pos(self) -> int:
        return self._y

    def __str__(self) -> str:
        return f"Sun(name={self._name}, mass={self._mass}, pos=({self._x}, {self._y}))"