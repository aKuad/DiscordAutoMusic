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
""":information_source: Info of current playing music.
> :file_folder: **`FileName`**: {}
> :musical_note: **`Title   `**: {}
> :bust_in_silhouette: **`Artist  `**: {}
> :calendar_spiral: **`Release `**: {}
> :left_right_arrow: **`Duration`**: {}"""

# Function definitions
async def info(message: Message, vcls: DiscordVClients):
  # Get music metadata
  mdata = information(vcls.getVCliCurMusic(message.guild.id))

  # Message reply
  await message.reply(INFO_MES.format(mdata.get("File:FileName"),
                                      mdata.get("ID3:Title"),
                                      mdata.get("ID3:Artist"),
                                      mdata.get("ID3:RecordingTime"),
                                      mdata.get("Composite:Duration")).replace("None\n", "*None*\n"))

  # Quit
  return
