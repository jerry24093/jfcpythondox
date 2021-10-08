# Jerry
# Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

nBonker = mc.player.getTilePos()
mc.postToChat(nBonker)
