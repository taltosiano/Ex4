class Edge:

    def __init__(self, src: int, dst: int, weight: float):
        self.__src = src
        self.__dst = dst
        self.__weight = weight
        self.__info = ""
        self.__tag = 0

    def get_src(self) -> int:
        return self.__src

    def get_dst(self) -> int:
        return self.__dst

    def get_weight(self) -> float:
        return self.__weight

    def __repr__(self):
        return "%s" % (
            self.__weight)
