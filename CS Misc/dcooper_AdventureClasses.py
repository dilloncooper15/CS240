from items import *


class Room:
    def __init__(self, name, exits, items, objects):
        self.name = name
        self.exits = exits
        self.items = items
        self.objects = objects

    def exit(self, outside):
        self.exits = outside

    def append_item(self, item):
        self.items.append(item)

    def remove(self, obj):
        for thing in self.room:
            pass

    def __str__(self):
        return '\nYou\'re in the {}'.format(self.name)
        # return '{} {}'.format(self.name, self.exits, self.items, self.objects)

Porch = Room('Porch', {}, [], [])
Foyer = Room('Foyer', {}, [], [])
Chapter = Room('Chapter', {}, [], [])
FirstRound = Room('FirstRound', {}, [], [])
Landing = Room('Landing', {}, [], [])
SecondRound = Room('SecondRound', {}, [], [])
ThirdFloorHallway = Room('ThirdFloorHallway', {}, [], [])
ThirdRound = Room('ThirdRound', {}, [], [])
PresidentRoom = Room('PresidentRoom', {}, [], [])
Basement = Room('Basement', {}, [], [])
BasementRound = Room('BasementRound', {}, [], [])
Kitchen = Room('Kitchen', {}, [], [])
BarRoom = Room('BarRoom', {}, [], [])
BackYard = Room('BackYard', {}, [], [])


Porch.exits = ({'North': Foyer})
Foyer.exits = ({'North': Chapter,
                'South': Porch,
                'West': FirstRound,
                'Up': Landing,
                'Down': Basement})
Chapter.exits = ({'South': Foyer})
FirstRound.exits = ({'East': Foyer})
Landing.exits = ({'North': SecondRound,
                  'Down': Foyer,
                  'Up': ThirdFloorHallway})
SecondRound = ({'South': Landing})
ThirdFloorHallway.exits = ({'North': ThirdRound,
                            'Down': Landing,
                            'East': PresidentRoom})
ThirdRound.exits = ({'South': ThirdFloorHallway})
PresidentRoom.exits = ({'East': ThirdFloorHallway})
Basement.exits = ({'North': BasementRound,
                   'Up': Foyer,
                   'East': BarRoom,
                   'West': Kitchen})
BarRoom.exits = ({'West': Basement,
                  'East': BackYard})
BackYard.exits = ({'West': BarRoom})
BasementRound.exits = ({'South': Basement})
Kitchen.exits = ({'East': Basement})


class Player:
    player_list = []

    def __init__(self, name):
        self.inventory = []
        self.health = 100
        self.weapon = None
        self.location = Porch
        Player.player_list.append(self)

    def move(self, request):
        if len(request) > 1:
            if request in self.location.exits.keys():
                self.location = self.location.exits[request]
                print(self.location)
            else:
                print('\nSorry, your request cannot be executed because you\
                    cannot go this way. Please select a different\
                    direction.\n')
        else:
            print('\nSorry, I do not recognize your request. Where do you\
             wish to go?\n')

    def append_to_inventory(self, request):
        if item in self.location.objects:
            if request[1] == item.name:
                print('\nThis is not an applicable object for your\
                    inventory.\n')
                return
            else:
                for item in self.location.items:
                    if request[1] == item.name:
                        self.inventory.append(item)
                        self.location.items.remove(item)
                        print('\nOkay.\n')
                        break
                    else:
                        print('\nThere is no {} here!\n'.format(request[1]))

    def attack(self, weapon, enemy):
        for thing in self.inventory:
            if thing.name == weapon:
                weapon = thing
                break
        enemy.health -= weapon.damage
        self.room.remove(Leo)


if __name__ == '__main__':
    var = Player('Dillon')
