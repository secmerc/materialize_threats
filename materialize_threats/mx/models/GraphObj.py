from abc import ABC


class GraphObj(ABC):
    def __init__(self, sid, gid, value):
        self.sid = sid
        self.gid = gid
        self.value = value


    def enrich_from_graph(self, attrs):
        for e in attrs:
            self.__setattr__(e[0], e[1])
