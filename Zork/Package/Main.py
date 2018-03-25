# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:55:56 2018

@author: Gregory
"""

import Street

game = Street.Street()

size = int(input("How big is the street?\n"))

game.createStreet(size)

game.interface()