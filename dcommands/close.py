# coding: UTF-8
#
# dcommands/close.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients
from datetime import time


# Function definitions
async def close(message: Message, vcls: DiscordVClients, com: list):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Bot's voice connection check
  if message.guild.voice_client == None or not vcls.isVCliExist(message.guild.id):
    await message.reply(":stop_sign: Not connected to voice channel yet. Aborting.")
    return

  # If not setted closing music
  if vcls.getVCliCloseMusic() == "":
    await message.reply(":stop_sign: Sorry, but closing music is not specified by moderator. To use this function, please contact to moderator.")
    return

  # When not specified optional argument
  if len(com) == 2:
    ctime = vcls.getVCliClose(message.guild.id)
    if ctime[0]:
      await message.reply(":clock3: Current closing time is between %d:%02d to %d:%02d." % (ctime[1].hour, ctime[1].minute, ctime[2].hour, ctime[2].minute))
    else:
      await message.reply(":infinity: Now closing time is not setted.")
    return
  else:
    # Try to process argument
    try:
      cst = com[2].split(':')
      ced = com[3].split(':')
      cst = time(int(cst[0]), int(cst[1]))
      ced = time(int(ced[0]), int(ced[1]))
    except:
      await message.reply(":stop_sign: Invalid argument. Aborting.")
      return
    # Set closetime data
    if cst != ced:
      vcls.setVCliClose(message.guild.id, True, cst, ced)
      await message.reply(":white_check_mark: Closing time set to %d:%02d - %d:%02d." % (cst.hour, cst.minute, ced.hour, ced.minute))
      return
    else:
      vcls.setVCliClose(message.guild.id, False, time(0, 0), time(0, 0))
      await message.reply(":white_check_mark: Closing time set to disabled.")
      return
