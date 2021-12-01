# coding: UTF-8
#
# dcommands/skip.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients


# Function definitions
async def skip(message: Message, vcls: DiscordVClients):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Bot's voice connection check
  if message.guild.voice_client == None or not vcls.isVCliExist(message.guild.id):
    await message.reply(":stop_sign: Not connected to any voice channel yet. Aborting.")
    return

  # Skip current playing music
  if vcls.skipMusic(message.guild.id):
    await message.reply(":track_next: Skipped current playing music.")
  else:
    await message.reply(":stop_sign: Something went wrong.")

  # Quit
  return
