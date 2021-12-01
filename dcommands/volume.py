# coding: UTF-8
#
# dcommands/volume.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients


# Function definitions
async def volume(message: Message, vcls: DiscordVClients, com: list):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Bot's voice connection check
  if message.guild.voice_client == None or not vcls.isVCliExist(message.guild.id):
    await message.reply(":stop_sign: Not connected to voice channel yet. Aborting.")
    return

  # When not specified optional argument
  if len(com) == 2:
    # Print current volume
    mvol = vcls.getVCliVol(message.guild.id)
    await message.reply(":level_slider: Current volume is **%.2f**." % mvol)
  else:
    # Check option argument of volume
    try:
      mvol = float(com[2])
      if mvol < 0.0 and 1.0 < mvol:
        await message.reply(":stop_sign: Volume must be set between 0.0 to 1.0. Aborting.")
        return
    except:
      await message.reply(":stop_sign: Invalid argument of volume. Aborting.")
      return
    # Set volume
    if vcls.setVCliVol(message.guild.id, mvol):
      await message.reply(":white_check_mark: Volume set to %.2f. Accept from next music." % mvol)
    else:
      await message.reply(":stop_sign: Something went wrong.")

  # Quit
  return
