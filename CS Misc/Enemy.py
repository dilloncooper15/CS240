class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def alive(self):
        return self.health > 0


class Leo(Enemy):
    def __init__(self):
        super().__init__("Leo", 10, 1)
