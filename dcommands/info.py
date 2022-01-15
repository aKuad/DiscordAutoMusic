# coding: UTF-8
#
# dcommands/info.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
from discord import Message
from dcommands.DiscordVClients import DiscordVClients
from pyexifinfo import information


# Messages definitions
INFO_MES = \
""":information_source: Information of current playing music.
> :file_folder: **`FileName`**: {}
> :musical_note: **`Title   `**: {}
> :bust_in_silhouette: **`Artist  `**: {}
> :calendar_spiral: **`Release `**: {}
> :left_right_arrow: **`Duration`**: {}"""

# Function definitions
async def info(message: Message, vcls: DiscordVClients):
  # User's voice connection check
  if message.author.voice == None:
    await message.reply(":stop_sign: You aren't connected to voice channel. Aborting.")
    return

  # Bot's voice connection check
  if message.guild.voice_client == None or not vcls.isVCliExist(message.guild.id):
    await message.reply(":stop_sign: Not connected to voice channel yet. Aborting.")
    return

  # Get music metadata
  mdata = information(vcls.getVCliCurMusic(message.guild.id))

  # If voice client is not available
  if mdata == None:
    await message.reply(":stop_sign: Something went wrong.")

  # Message reply
  await message.reply(INFO_MES.format(mdata.get("File:FileName"),
                                      mdata.get("ID3:Title"),
                                      mdata.get("ID3:Artist"),
                                      mdata.get("ID3:RecordingTime"),
                                      mdata.get("Composite:Duration")).replace("None\n", "*None*\n"))

  # Quit
  return
