#Welcome to the interpreter
#Please help in completeing the actions


class action(object): #parrent class

	def doAction(self, recipient):
		print "dummy function you should never see this if you did you did something wrong."

nullStr = "dummy"
class attack(action): 

	def doAction(self, recipient): #IMPORTANT: fill in later
		pass

class north(action):

	def doAction(self, nullStr): #IMPORTANT: fill in later
		pass

class south(action):

	def doAction(self, nullStr): #IMPORTANT: fill in later
		pass

class east(action):

	def doAction(self, nullStr): #IMPORTANT: fill in later
		pass

class west(action):

	def doAction(self, nullStr): #IMPORTANT: fill in later
		pass

class openMenu(action):

	def doAction(self, nullStr): #IMPORTANT: Put Andrew's menu code here
		pass

class pickUp(action):

	def doAction(self, recipient): #IMPORTANT: fill in later
		pass

class openInventory(action, scene):

	def doAction(self, nullStr): #VERY IMPORTANT: integrate a new class that allows the player to do things with their inventory
		pass

	def action(): #VERY IMPORTANT: get this scene done
		pass

class showStats(action):

	def doAction(self, recipient): #IMPORTANT: fill in later
		pass

class command(engine):
	actions = []
	entities = []
	action = ""
	recipient = ""

	for i in range(self.sceneList.length()): #sets all of the entites that actions can be called on  
		if isInstance(obj, hostileEntity) or isInstance (obj, item):
			entities.append(self.sceneList[i])

	def __init__(self, rawCommand):
		self.rawCommand = rawCommand #this is the raw string that 

	def parseCommand(self): #converts the length to something readable

		words = []
		currentWord = ""
		for i in range(rawCommand.length()): #parses everything	
			if rawCommand[i] != " ":
				currentWorld += rawCommand[i]
			else:
				words.append(currentWord)
				currentWord = ""

			selectedAct = False
			selectedEnt = False
		for i in range(words.length()): #converts it into transatable material
			tranSelectedAct = False
			
			for j in range(actions.length()): #parses the actions
				if words[i] == actions[j].name and !selectedAct: #then checks
					action = actions[j]
					tranSelectedAct = True
					selectedAct = True
					break

			if !tranSelectedAct: #skips if word has already
				for j in range(entities.length()):
					if words[i] == entities[j].name and !selectedEnt:
						recipient = entities
						selectedEnd = True
						break

		if selectedAct and selectedEnt: #runs the command that the user wants to parse
			action.doAction(recipient)

		elif selectedAct and !selectedEnt: #runs commands if they do not have a specified target
			action.doAction("dummy")

		else:
			return "sorry %s is an invalid command." % rawCommand
