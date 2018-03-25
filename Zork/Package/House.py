# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""
class House :
    import Monster
    from random import randint
    
    monsterList = []
    
    numMonsters = randint(0, 10)
    hasChanged = 0
    numPeople = 0
    
    observers = []
    
    def createMonsters(self) :
        from random import randint
        import Monster
        for x in range (0, self.numMonsters) :
            monGen = randint(1, 5)
            monster = Monster.Monster()
            if monGen == 1 :
                monster = Monster.Zombie()
                if monGen == 2 :
                    monster = Monster.Vampire()
                if monGen == 3 :
                    monster = Monster.Ghoul()
                if monGen == 4 :
                    monster = Monster.WereWolf()
                    
            monster.addObserver(self)
            self.monsterList.append(monster)
    
    def attack(self, candy, attack) :
            for x in range(0, self.numMonsters) :
                self.monsterList[x].takeDamage(candy, attack)
                
    def monsterAttack(self) :
        damage = 0.0
        for x in range(0, self.numMonsters) :
                damage = damage + self.monsterList[x].attack
    
        return damage
    
    def update(self, position) :
        import Monster
        self.numPeople += 1
        
        tempMonster = Monster.Person()
        self.monsterList[position] = tempMonster
        
        if self.numPeople >= self.numMonsters :
            self.notifyObservers()
        
    def addObserver(self, newObserver) :
        self.observers.append(newObserver)
           
    def notifyObservers(self) :
        for x in self.observers :
            self.observers[x].update()
            
    def look(self) :
        print ("You see: ")
        for x in range(0, self.numMonsters) :
            print ("%s, " %self.monsterList[x].getName())
        print ("\n")
        
    
    
        
