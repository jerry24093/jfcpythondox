'''
mcdemo.placeblock.py
Get the player tile position and save it to a variable
Use the function to place a block under your current position
(under you is Y - 1)
'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
mc.setBlock(x, y, z, blockTypeID)