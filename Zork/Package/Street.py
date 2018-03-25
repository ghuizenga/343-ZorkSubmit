# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""
class Street :
    
    import Player, Monster, Item, House
    
    adventurer = Player.Player()
    streetMap = []
    mapSize = 0
    playerPosition = 0
    housesCleared = 0
    endCondition = 0
    playerInside = 0
    
    def createStreet(self, size) :
        import House
        self.mapSize = size - 1
        self.adventurer.fillInv()
        
        for x in range (0, size) :
            house = House.House()
            house.createMonsters()
            house.addObserver(self)
            self.streetMap.append(house)
            
        
    def gameEnd(self, result) :
        if result == 0 :
            print("You've been gobbled up, GAME OVER\n")
        if result == 1 :
            print("Congratulations, you've saved candy street!\n")
        
        self.endCondition = 1
    
    def playerMove(self, direction) :
        if direction == 0 :
            if self.playerPosition > 0 :
                self.playerPosition -= 1
                print("you move one house to the left, you're at house # %d\n" 
                              %self.playerPosition)
            else:
                print("you are at the leftmost house, you can't go further left\n")
        
        if direction == 1 :
            if self.playerPosition < self.mapSize :
                self.playerPosition += 1
                print("you move one house to the right, you're at house # %d\n"
                              %self.playerPosition)
            else:
                print("you're at the rightmost house, you can't go further right\n")
    
    def Update(self) :
        self.housesCleared += 1
        if self.housesCleared >= self.mapSize :
            self.gameEnd(1)
    
    def interface(self) :
        while self.endCondition != 1 :
            if self.playerInside == 1 :
                print("You're standing outside house # %d on candy street\n" 
                              %self.playerPosition)
                print("You have %d hp\n" %self.adventurer.getHp())
                answer = input("What do you do? (move left, move right, go inside)\n")
                
                if answer == "move left" :
                    self.playerMove(0)
                if answer == "move right" :
                    self.playerMove(1)
                if answer == "go inside" :
                    self.playerInside = 0
                if answer == "quit" :
                    self.gameEnd(0)
                    exit
                
            else:
                print("You're standing inside house # %d\n" %self.playerPosition)
                print("You have %d hp\n" %self.adventurer.getHp())
                self.streetMap[self.playerPosition].look()
        
                answer = input("\nWhat do you do? (fight, flee, wait)\n")
                if answer == "fight" :
                    self.adventurer.checkItems()
                    answer = int(input("Which weapon do you use? (number)\n"))
                    if answer < len(self.adventurer.inventory) and answer >= 0 :
                        if self.adventurer.inventory[answer].get_name() != "nothing" :
                            print("You attack with the %s\n"%self.adventurer.inventory[answer])
                            self.streetMap[self.playerPosition].attack(self.adventurer.
                                    inventory[answer],self.adventurer.damage)
                            self.adventurer.inventory[answer].lose_durability()
                        else:
                            print("You can't attack with nothing\n")
                if answer == "flee" :
                    print("You flee outside\n")
                    self.playerInside = 1
                if answer == "wait" :
                    print("You wait\n")
                if answer == "quit" :
                    self.gameEnd(0)
                    exit
                if self.playerInside == 0 :
                    self.adventurer.takeDamage(self.streetMap[self.playerPosition].monsterAttack())
                if self.adventurer.getHp() <= 0:
                    self.gameEnd(0)
                    exit
            
                
                    
                    
            
            
    