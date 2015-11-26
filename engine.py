class engine(Object): #the engine is where
	
	def __init__(self, sceneList, currentScene, worldVars):
		self.sceneList = sceneList #all of the scenes are here
		self.currentScene = currentScene #this is the scene that is currently being used
		self.worldVars = worldVars #the variables that the whole world has attached to it


	def playScene(): #plays the scene
		currentScene.action()

	def nextScene(sceneNum): #runs the next scene
		currentScene = sceneList[sceneNum]

	def play(): # this is where the game will be played from
		pass
