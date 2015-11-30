import random

class worldMap(object):
  
  def __init__(self, Map):
    self.Map = Map
    
  def populateRandomly(self, enemy):
    xcord = random.randint(len(Map))
    ycord = random.randint(len(Map[0]))
    Map[xcord][ycord].entities.append(enemy)
    
class chunk(scene): #one part of the map that is stored
  
  def __init__(self, entities, items, name, objectives):
    self.name = name #name of the chunk
    self.entities = entities #list containing the specific enemies in the chunk
    self.items = items #list containing the items in the chunk
    self.objectives = objectives #list containing the main objectives in the chunk
    
class objective(object): #tasks or quests that the player must complete in order to win
    
  def __init__(self, completed)
    self.completed = completed
      
  def onComplete(self): #this is an action that occurs upon completion
    return "this is a dummy function you should NEVER see this (onComplete)"

class entity(object): #this is where all of the entities are located, these 

  def __init__(self, gold, level, xp, inventory, equippedItem, currentHealth, health, defense, attack, name, position):
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
    
  def levelUp(self):
    if xp >= level * 100:
      xp -= level * 100
      level += 1
      
  def attack(self, target):
    if isinstance(entity, target):
      target.currentHealth -= self. equippedItem.useageDamage
    else:
      return "That is not a valid target"
    
    
class item(self): #items are anything that the player can interact with and they can aid the player in various ways
  
  def __init__(self, itemType, statModifier, modifiedStat, itemName, useageDamage): 
    self.itemType = itemType
    self.statModifier = statModifier
    self.modifiedStat = modifiedStat
    self.itemName = itemName
    self.useageDamage = useageDamage
  
  def applyEffects(self, condition, target, onUseEffects): #this is how things are attacked and potions are added and other stuff
    if condition:
      return "Dummy function you should never see"
  
  
