import random
from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Instantiating People
player1 = Person("Valos", 3460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
player2 = Person("Nick", 4460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
player3 = Person("Robot", 3260, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person("Magus", 1200, 65, 45, 25, [])

players = [player1, player2, player3]

print("AN ENEMY ATTACKS!")

running = True
while running:
    print("====================")
        
    print("\n \n")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(player.name + " attacked for", dmg, " points of damage")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            
            current_mp= player.get_mp()

            if spell.cost > current_mp:
                print("\nNot enough MP\n")
                continue
            
            player.reduce_mp(spell.cost)

            if spell.type == "White":
                player.heal(magic_dmg)
                print("\n" + spell.name + " heals for", str(magic_dmg), "HP.")
            elif spell.type == "Black":
                enemy.take_damage(magic_dmg)
                print("\n" + spell.name + "deals", str(magic_dmg), "points of damage")

    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemy.generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks " + players[target].name + " for: ", enemy_dmg)

    print("==========================")
    print("Enemy HP:" + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))
 
    if enemy.get_hp() == 0:
        print("You win")
        running = False
    elif player.get_hp() == 0:
        print("Your enemy has defeated you!")
        running = False