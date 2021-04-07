#!/usr/bin/python3

import random
import math

# Warrior & Battle Class
class Warrior:

    def __init__(self, name="Warrior", health=0, attMax=0, blockMax=0):
        self .name = name
        self .health = health
        self .attMax = attMax
        self .blockMax = blockMax

    def attack(self):
        attAmt = self.attMax * (random.random() + .5)
        return attAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):
        
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        
        warriorAAttAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attakcs {} and deals {} damage" .format(warriorA.name, warriorB.name, damage2WarriorB))

        print("{} is down to {} health" .format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious" .format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    
    Franciscus = Warrior("Franciscus", 100, 50, 30)
    
    Julianis = Warrior("Julianis", 100, 40, 40)

    battle = Battle()

    battle.startFight(Franciscus, Julianis)

main()

# Warriors will have names, healt and attack & block maximus
#They will have the capabilities to attack & block random amount

# Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random()

# Battle Class capability of looping until 1 warrior dies
# Warrios will each get a turn to attack each other

# Function gets 2 warriors
# 1 warrior attacks the other
# Attacks & Blocks be integers

