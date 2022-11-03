# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Player: 
  def __init__(self , player_num = 1):
    self.player_num = player_num
    self.lives = 3
    self.movement = keyboard 
    self.x_coord = x_coord
    self.y_coord = y_coord

## Class Interface 2

class Enemy: 
  def __init__(self):
    self.hits_to_kill = 1 
    self.postion = random 
    self.alive = True
    
## Class Interface 3

class Background:
  def __init__(self):
    self.grass = []
    self.color = 'green'
    self.treats = []