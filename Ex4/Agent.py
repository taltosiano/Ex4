class Agent:

    def _init_(self, id: int, value: float, src: int, dest: int, speed: float, pos: tuple) -> None:
        self._id: int = id
        self._value: float = value
        self._src: int = src
        self._dest: int = dest
        self._speed: float = speed
        self._pos: tuple = pos

    def get_id(self):
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_value(self):
        return self._value

    def set_value(self, value: float) -> None:
        self._value = value

    def get_src(self):
        return self._src

    def set_src(self, src: int) -> None:
         self._src = src

    def get_dest(self):
        return self.dest

    def set_dest(self, dest: int) -> None:
        self._dest = dest

    def get_speed(self):
        return self.speed

    def set_speed(self, speed: float) -> None:
        self._speed = speed

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple) -> None:
        self._pos = pos

    def _repr_(self) -> str:
        return "{{'Agent': id:{} value:{} src:{} dest:{} speed:{} pos:{}}}" \
            .format(self._id, self._value, self._src, self._dest, self._speed, self._pos)