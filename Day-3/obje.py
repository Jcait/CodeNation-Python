class Attack:
    sword = "You attack with the sword"
    shield = "You block the attack"

class Mage:
    def __init__(self, name, robes, spell):
        self.name = name
        self.robes = robes
        self.spell = spell
        self.shield = Attack.shield

    def __name__(self):
        return "Mage"

    def __str__(self):
        return f"{self.name} is a {__name__}"

class Spells:
    fireball = "Fireball"
    lightning = "Lightning"
    raise_dead = "Raise Dead"


atk = Attack()

print(Attack.sword)
print(atk.sword)

merlin = Mage( "Merlin","Arcane", Spells.fireball)
merlin.age = 22
print(f"{merlin.name} casts {merlin.spell} empowered by his {merlin.robes} despite being {merlin.age} old")
print(merlin)
