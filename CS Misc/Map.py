import Items
import Enemy


class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class Outside(Map):
    def introduction(self):
        return """
        You are facing a massive green house with a long
        stone walkway that leads to concrete steps. Small lanterns
        on each side of the walkway create an eerie glow, and are
        your only source of light. Long vines encase the house,
        hanging down to conceal most of the porch. The steps lead
        to a heavy wooden door that sits back in the shadows of
        the archway.\n
        You hear muffled sounds coming from the house.
        """

    def modify_player(self, player):
        pass


class Foyer(Map):
    pass
