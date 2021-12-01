# coding: UTF-8
#
# dcommands/stop.py
#
# Author: akuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients


# Function definitions
async def stop(message: Message, vcls: DiscordVClients):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Disconnecting when connection
  if vcls.delVCli(message.guild.id):
    if message.guild.voice_client != None:
      await message.guild.voice_client.disconnect()
    await message.reply(":stop_button: Stop playing.\n:white_check_mark: Successfully disconnected.")
  else:
    await message.reply(":stop_sign: Not connected to any voice channel. Aborting.")
  return
