import json
import sqlite3


def load_db(dbfile):
    ret = None
    room_dict = {}

    con = sqlite3.connect(dbfile)
    for id, jsontext in con.execute("select id, json from rooms"):
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
        room_dict[id] = ret

    con.close()

    return room_dict


class Item():
    """The base class for all items."""

    def __init__(self, name, descript):
        self.name = name
        self.descript = descript

    def __str__(self):
        return "\n{}: {}\n".format(self.name, self.descript)


class Room():
    def __init__(self, id=0, name="A Room", description="An empty room",
                 neighbors={}, inv=[], flavorsentences=" "):
        self.ident = id
        self.name = name
        self.description = description
        self.neighbors = neighbors
        self.inv = []
        self.flavorsentences = " "
        self.visited = False
        for item in inv:
            self.inv.append(Item(**item))

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')
