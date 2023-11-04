from Player import *

class Soldier(Player):
    attack = 100

    naechsterSoldier = None

    def __init__(self, healthToGiveToPlayer, atk):
        super().__init__(healthToGiveToPlayer)
        self.attack = atk


    # def HolMirDieSoldiers(self):
    #     # fueg soldier irgendwo hinzu oder so...
    #     # self.naechsterSoldier
    #
    #     if self.naechsterSoldier is None:
    #         return
    #     else:
    #         self.HolMirDieSoldiers(self)



    # def __init__(self):
    #     pass


# s1 = Soldier()
# s1.naechsterSoldier = Soldier()

s1 = Soldier(100,200)

s1.fight()

print(s1.health)
print(s1.attack)



# reflection

print(type(3))
print( getattr(s1, "attack") )

# gibt neuen attribut mit namen testattribut
setattr(s1, "testattribut", "DerWertDesTestAttributs")


print( getattr(s1, "testattribut") )

# fragt ob s1 Typ von Klasse Soldier ist
print(type(s1) is Soldier )