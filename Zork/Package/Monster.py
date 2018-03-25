# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""
class Monster :
    import random
    
    name = "monster"
    hp = 0
    attack = 0
    immunities = [5, 5]
    weakness = 5
    modifier = 1
    randMod = 1.0
    damage = 0.0
    
    hasChanged = 0
    observers = []
    
    def takeDamage(self, weapon, playerAttack):
        if self.name == "Person" :
            return;
        
        for x in range(0, 4) :
            if weapon == self.immunities[x]:
                print ("%s is immune to your attack!\n" % self.name)
                modifier = 0
                
        if weapon == self.weakness :
            if weapon == 1 :
                print ("%s is weak to SourStraws!\n" % self.name)
                modifier = 2
            if weapon == 3 :
                print ("%s is weak to NerdBombs!\n" % self.name) 
                modifier = 5
                    
        if weapon == 0 :
            randMod = 1.00
        if weapon == 1 :
            randMod = round(self.random.uniform(1.00, 1.75), 3)
        if weapon == 2 :
            randMod = round(self.random.uniform(2.00, 2.40), 3)
        if weapon == 3 :
            randMod = round(self.random.uniform(3.50, 5.00), 3)
            
        damage = playerAttack * modifier * randMod
        self.hp = self.hp - damage
        print ("%s takes %f damage!\n\n" %(self.name, damage))
        
        if self.hp <= 0 :
            print ("%s is defeated and turns into a person!\n\n" %(self.name))
            self.setChanged(self)
            self.notifyObservers(self)
            self.defeated()
    
    def attack(self) :
        return self.attack
    
    def getName(self) :
        return self.name
    
    def defeated(self) :
        self.name = "Person"
        self.attack = -1
        
    def addObserver(self, newObserver) :
        self.observers.append(newObserver)
    
    def setChanged(self) :
        if self.hasChanged == 0 :
            self.hasChanged == 1
            return
        if self.hasChanged == 1 :
            self.hasChanged == 0
            return

    def notifyObservers(self) :
        if self.hasChanged == 1 :
            for x in self.observers :
                self.observers[x].update()

class Person(Monster) :
    
    name = "Person"
    hp = 100
    attack = -1

class Zombie(Monster) :
    import random
    
    name = "Zombie"
    hp = random.randint(50, 101)
    attack = random.randint(0, 11)
    weakness = 2

class Vampire(Monster) :
    import random
    
    name = "Vampire"
    hp = random.randint(100, 201)
    attack = random.randint(10, 21)
    immunities = [1, 5]

class Ghoul(Monster) :
    import random
    
    name = "Ghoul"
    hp = random.randint(40, 81)
    attack = random.randint(15, 31)
    weakness = 3

class WereWolf(Monster) :
    import random
    
    name = "WereWolf"
    hp = 200
    attack = random.randint(0, 41)
    immunities = [1, 2]
    
        
        