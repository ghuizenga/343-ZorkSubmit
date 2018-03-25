# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""
class Player :
    import random, Item
    
    hpMax = random.randint(100,126)
    currentHp = hpMax
    damage = random.randint(10, 21)
    
    inventory = []
    observers = []
    
    def fillInv(self) :
        import Item, random
        item = Item.hersheys_kisses(0)
        self.inventory.append(item)
        for x in (1, 10) :
            gen = random.randint(1,4)
            if gen == 1 :
                item = Item.sour_straws(x)
            if gen == 2 :
                item = Item.chocolate_bars(x)
            if gen == 3 :
                item = Item.nerd_bombs(x)
            item.add_observer(self)
            self.inventory.append(item)
        
    
    def update(self, item) :
        import Item
        print("Your %s have run out!\n" %self.inventory[item].getName())
        newItem = Item()
        self.inventory[item] = newItem
    
    def getHp(self) :
        return self.currentHp
        
    def checkItems(self) :
        for y in range (0, 10) :
            print("%d\: %s "%(y, self.inventory[y].get_name()))
    
    def takeDamage(self, monsterDamage) :
        self.currentHP = self.currentHP - monsterDamage
        print("You take %d damage as the monsters attack!\n" % monsterDamage)
        
        if self.currentHP > self.hpMax :
            self.currentHP == self.hpMax
        if self.currentHP <= 0 :
            self.notifyObservers(self, 0)
    
    def addObserver(self, newObserver) :
        self.observers.append(newObserver)
    
    def notifyObservers(self, result) :
        for x in self.observers :
            self.observers[x].update(result)
    
    
