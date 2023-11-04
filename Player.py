

class Player:
    health = 100

    # private
    __speed = 20

    # protected
    _money = 20

    def __init__(self, healthToGiveToPlayer):
        self.health = healthToGiveToPlayer

    def fight(self):
        self.health -= 10

