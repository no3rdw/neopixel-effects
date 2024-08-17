import time
# This is a class template applied to all other defined Effects (including the Menu)

class Effect:
	def __init__(self, device:Device):
		self.name = 'Effect'
		self.device = locals()['device']

		#device.clearDisplayGroup(device.effect_group)

		#self.menu = [
			#{
			#	'label': 'Setting',
			#	'set': self.setFunction,
			#	'get': self.getFunction
			#}
        #]
		#self.lastFrame = 0

	def play(self):
		if (self.device.limitStep(.1, self.lastFrame)):
			# do stuff
			
			self.lastFrame = time.monotonic()

	def handleRemote(self, key:str):
		print(key)
		if key == 'Enter':
			pass