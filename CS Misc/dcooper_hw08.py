class Pet:
    """ Defines Pet class. """
    def __init__(self, name, age, price):
        """(str, int, float) -> None
        Initializes the Pet class with a string name, integer age and float \
        price.
        """
        self.name = name
        self.age = int(age)
        self.price = float(price)

    def __str__(self):
        """ (Pet) ->
        """
        return self.name

    def __repr__(self):
        return 'Pet ({}, {}, {})'.format(self.name, self.age, self.price)

    def __eq__(self, obj):
        return self.name == obj.name and \
            self.age == obj.age and \
            self.price == obj.price

    def discount(self, percent):
        self.price = self.price - (self.price * percent)

    def make_sound(self):
        print("Not implemented.")


class Dog(Pet):
    """ Defines Dog class which is a subclass of Pet. """
    def __init__(self, name, age, price, breed):
        super().__init__(name, age, price)
        self.breed = breed

    def __str__(self):
        return super().__str__() + ' ({})'.format(self.breed)

    def __repr__(self):
        return 'Dog({}, {}, {}, {}'.format(
            self.name, self.age, self.price, self.breed)

    def __eq__(self, obj):
        return super().__eq__() and self.breed == obj.breed
        # return self.name == obj.name and \
        #     self.age == obj.age and \
        #     self.price == obj.price and \
        #     self.breed == obj.breed

    def make_sound(self):
        print('Bark! Bark! Bark!')


class Fish(Pet):
    """ Defines Fish class which is a subclass of Pet. """
    def __init__(self, name, age, price, saltwater, species):
        super().__init__(name, age, price)
        self.species = species
        self.saltwater = saltwater

    def __str__(self):
        output = ''
        if self.saltwater:
            output += 'saltwater '
        output += super().__str__()
        output += ' ({})'.format(self.species)
        return output

    def __repr__(self):
        return 'Fish({}, {}, {}, {}, {}'.format(
            self.name, self.age, self.price, self.species, self.saltwater)

    def __eq__(self, obj):
        return self.name == obj.name and \
            self.age == obj.age and \
            self.price == obj.price and \
            self.saltwater == obj.saltwater and \
            self.species == obj.species

    def make_sound(self):
        print('Bark! Bark!... I mean(clears gills)... blurp..., blurp...')


if __name__ == '__main__':
    d = Dog('woof', 5, 50, 'Mutt')
    print(d)
    print(str(d))
    d.discount(0.05)
    print(d)
    print(str(d))
    d.make_sound()
    p = Fish('woof', 5, 50, True, 'Dogfish')
    print(p)
    print(str(p))
    p.discount(0.05)
    print(p)
    print(str(p))
    p.make_sound()
    print(d.price, p.price)
