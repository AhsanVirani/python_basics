import random
from .magic import Spell

class bcolors:
    HEADER = '\003[95m'
    OKBLUE = '\003[94m'
    OKGREEN = '\003[92m'
    WARNING = '\003[93m'
    FAIL = '\003[91m'
    ENDC = '\003[0m'
    BOLD = '\003[1m'
    UNDERLINE = '\003[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magics"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + self.name + ":")
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell.name, "cost:", str(spell.cost))
            i += 1

    def get_stats(self):
        print(self.name + "     " + str(self.hp) + "/" + str(self.maxhp) + "        " 
        + str(self.mp) + "/" + str(self.maxmp))
    