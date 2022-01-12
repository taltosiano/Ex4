class Pokemon:
    def __init__(self, _value: float, _type: int, _pos: tuple):
        self._type = _type
        self._value = _value
        self._pos = _pos

    def get_value(self) -> float:
        return self._value

    def get_type(self) -> int:
        return self.get_type()

    def get_pos(self) -> tuple:
        return self._pos

    def set_pos(self, pos: tuple) -> None:
        self._pos = pos

    def __repr__(self):
        return f"value: {self._value}, type: {self._type}, pos: {self._pos}"
