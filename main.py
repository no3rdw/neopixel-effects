from device import Device
device = Device()
from menu import Menu

if device.writeMode == True:
	from settings import Settings
	effects = ['Settings']
else:	
	from static import Static
	from itysl import ITYSL
	from sky import Sky
	from cards import Cards
	effects = ['Cards','Sky','ITYSL','Static']

# https://learn.adafruit.com/circuitpython-display-support-using-displayio/library-overview

menu = Menu(device)
if device.writeMode == True:
	device.changeEffect('Settings')
else:
	device.changeEffect(device.saveData['selectedEffect'])

device.gc()

while True:
	keys = device.neokey.get_keys() # using this is MUCH faster than referencing device.neokey[x] over and over 
	if device.menu_group.hidden and keys[0] and device.limitStep(device.buttonPause, device.lastButtonTick): # only enter this loop if menu button is down
		device.setLastButtonTick()
		menu.showMenu()

	if not device.menu_group.hidden: # only play the menu loop if menu is open
		menu.play()

	device.effect.play()