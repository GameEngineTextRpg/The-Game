import random

class worldMap(object):
  
  def __init__(self, Map):
    self.Map = Map
    
  def populate(self, enemy):
    xcord = random.randint(len(Map))
    ycord = random.randint(len(Map[0]))
    Map[xcord][ycord].entities.append(enemy)
    
class chunk(scene): #one part of the map that is stored
  
  def __init__(self, entities, items):
    self.entities = entities
    self.items = items

class entity(object): #this is where all of the entities are located, these 

  def __init__(self, gold, level, xp, inventory, equippedItem, currentHealth, health, defense, attack, name):
    self.gold = gold #in-game curency that is used to by items
    self.level = level #self explanitory
    self.xp = xp #in game mechanic that is erned after every monster kill
    self.inventory = inventory #this is where all of the items that the player currently uses are located
    self.equippedItem = equippedItem #this is the weapon that you do damage with
    #stats that provide various modifiers throughout the battle
    self.currentHealth = currentHealth 
    self.health = health
    self.defense = defense
    self.attack = attack
    #name of your champion
    self.name = name
    
  
    
  def displayStats(self):
    print self.name
    print "health = %d/%d" % (self.currentHealth, self.health)
    print "defense = %d" % self.defense
    print "attack = %d" % self.attack
    print "equipped item = %s" % equippedItem.name
    print "level = %d" % self.level
    print "xp = %d" % self.xp
    print "gold = %d" % self.gold
    
class item(self): #items are anything that the player can interact with and they can aid the player in various ways
  
  def __init__(self, itemType, statModifier, modifiedStat, itemName):
    self.itemType = itemType
    self.statModifier = statModifier
    self.modifiedStat = modifiedStat
    self.itemName = itemName
  
  
  
