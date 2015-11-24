import json
import sqlite3


def load_db(dbfile):
    ret = None
    room_dict = {}

    con = sqlite3.connect(dbfile)
    for id, jsontext in con.execute("select id, json from rooms"):
        # jsontext = row[0]
        # print(jsontext)
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
        room_dict[id] = ret

    con.close()

    return room_dict


class Room():
    def __init__(self, id=0, name="A Room", description="An empty room",
                 neighbors={}):
        self.ident = id
        self.name = name
        self.description = description
        self.neighbors = neighbors
        self.visited = False

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    # def _description(self, direction):
    #     if direction in self.description:
    #         return self.description
    #     else:
    #         return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')
