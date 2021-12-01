# coding: UTF-8
#
# dcommands/play.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients


# Function definitions
async def play(message: Message, vcls: DiscordVClients, com: list):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Bot's voice connection check
  if message.guild.voice_client != None and vcls.isVCliExist(message.guild.id):
    await message.reply(":stop_sign: Already connected to voice channel. Aborting.")
    return

  # Check optional argument of volume
  if len(com) == 2:
    # If not
    vcli = await message.author.voice.channel.connect()
    vcls.addVCli(message.guild.id, vcli)
    await message.reply(":white_check_mark: Successfully connected.\n:level_slider: Volume set to **%.2f** (default).\n:file_folder: Now **%d** musics are available.\n:arrow_forward: Start playing." % (vcls.getVCliVol(message.guild.id), vcls.mCount))
  else:
    # If specified
    try:
      mvol = float(com[2])
      if mvol < 0.0 and 1.0 < mvol:
        await message.reply(":stop_sign: Volume must be set between 0.0 to 1.0. Aborting.")
        return
    except:
      await message.reply(":stop_sign: Invalid argument of volume. Aborting.")
      return
    vcli = await message.author.voice.channel.connect()
    vcls.addVCli(message.guild.id, vcli, mvol)
    await message.reply(":white_check_mark: Successfully connected.\n:level_slider: Volume set to **%.2f**.\n:file_folder: Now **%d** musics are available.\n:arrow_forward: Start playing." % (mvol, vcls.mCount))

  # Quit
  return
