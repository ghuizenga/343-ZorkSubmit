# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""
class Item(object) :
    
    name = "nothing"
    durability = 0
    max_durability = 0
    observers = []
    inv_slot = 0
    
    def lose_durability(self) :
        self.durability = self.durability - 1
        if self.durability <= 0 :
            self.notify_observers(self)
        
    def add_observer(self, inventory) :
        self.observers.append(inventory)
        
    def notify_observers(self) :
        for x in self.observers :
            x.update(self.inv_slot)
            
    def get_name(self) :
        return self.name
    
    def get_durability(self) :
        return self.durability
    
class hersheys_kisses(Item) :
        
    def __init__(self, inv) :
        self.name = "Hersheys Kisses"
        self.max_durability = 9001
        self.durability = 9001
        self.inv_slot = inv
    
    def lose_durability(self):
        pass

class sour_straws(Item) :
    
    def __init__(self, inv) :
        self.name = "Sour Straws"
        self.max_durability = 2
        self.durability = 2
        self.inv_slot = inv
    
class chocolate_bars(Item) :
    
    def __init__(self, inv) :
        self.name = "Chocolate Bars"
        self.max_durability = 4
        self.durability = 4

class nerd_bombs(Item) :
    
    def __init__(self, inv) :
        self.name = "Nerd Bombs"
        self.max_durability = 1
        self.durability = 1
        self.inv_slot = inv

