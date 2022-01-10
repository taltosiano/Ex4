class Node:

    def __init__(self, key: int, pos: tuple = None):
        self.__id = key
        self.__tag = 0
        self.__weight = 0
        self.__info = ""
        self.__pos = pos
        self.edges_in = 0
        self.edges_out = 0

    def get_id(self) -> int:
        return self.__id

    def get_pos(self) -> tuple:
        return self.__pos

    def set_pos(self, pos: tuple):
        self.__pos = pos

    def get_weight(self) -> int:
        return self.__weight

    def set_weight(self, w: int):
        self.__weight = w

    def get_info(self) -> str:
        return self.__info

    def set_info(self, i: str):
        self.__info = i

    def get_tag(self) -> int:
        return self.__tag

    def set_tag(self, t: int):
        self.__tag = t

    def __repr__(self):
        return str(self.__id) + ": |edges out| " + str(self.edges_out) + " |edges in| " + str(self.edges_in)
