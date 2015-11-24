class Item:
    """The base class for all items."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n====\n{}\nValue: {}\n".format(
            self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return "{}\n====\n{}\nDamage: {}".format(
            self.name, self.description, self.damage)


class Raid(Weapon):
    def __init__(self):
        super().__init__("Can of Raid",
                         "An insecticide used to eliminate unwanted pests", 1)


class Vacuum(Weapon):
    def __init__(self):
        super().__init__("Vacuum", "A portable, cordless vacuum", 5)


class Gun(Weapon):
    def __init__(self):
        super().__init__("Lazer Gun", "A gun that shoots lazers!", 2)


class Pencil(Weapon):
    def __init__(self):
        super().__init__("Pencil", "A freshly sharpened, stylish No. 2 pencil",
                         0)
