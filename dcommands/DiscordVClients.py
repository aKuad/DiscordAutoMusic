# coding: UTF-8
#
# dcommands/DiscordVClients.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
import discord
from subprocess import run, PIPE
from random import randint
from datetime import datetime, timezone, timedelta, time


# Class definitions
class DiscordVClients:
  # Field variables
  __clients = {}
  __mList = []
  __mClose = ""
  __mVolDef = 0.0
  mCount = 0


  # method - Constructor
  def __init__(self, mPath: str, mPathClose: str, mVolDef: float):
    # Field variables setting
    self.__mList = run("ls %s" % mPath, shell=True, stdout=PIPE)
    self.__mList = self.__mList.stdout.decode("UTF-8").strip().split("\n")
    self.__mClose = mPathClose
    self.__mVolDef = mVolDef
    self.mCount = len(self.__mList)
    # Quit
    return


  # method - A voice client addition
  def addVCli(self, gid: int, vCli: discord.VoiceClient, *vol):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      return False
    # Music volume variable set
    mVol = self.__mVolDef
    # Is argument of volume is specified
    if len(vol) != 0:
      try:
        mVol = float(vol[0])
        if mVol < 0.0 or 1.0 < mVol:
          return False
      except:
        return False
    # Voice client add
    self.__clients[gid] = {"vCli": vCli, "mVol": mVol, "mCur": "", "cEn": False, "cSt": time(0, 0), "cEd": time(0, 0)}
    print("A voice client created. Count: %d" % len(self.__clients))
    return True


  # method - A voice cliet exist checking
  def isVCliExist(self, gid: int):
    if self.__clients.get(gid) != None:
      return True
    else:
      return False


  # method - A voice client deletion
  def delVCli(self, gid: int):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      vc = self.__clients.pop(gid)
      # When playing, stop
      if vc["vCli"].is_playing():
        vc["vCli"].stop()
      print("A voice client deleted. Count: %d" % len(self.__clients))
      return True
    else:
      return False


  # method - A voice client volume set
  def setVCliVol(self, gid: int, mVol: float):
    # If specified volume is invalid
    if mVol < 0.0 or 1.0 < mVol:
      return False
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      self.__clients[gid]["mVol"] = mVol
      return True
    else:
      return False


  # method - A voice client volume get
  def getVCliVol(self, gid: int):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      return self.__clients[gid]["mVol"]
    else:
      return None


  # method - A voice client closing time info set
  def setVCliClose(self, gid: int, isen: bool, st: time, ed: time):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      self.__clients[gid]["cEn"] = isen
      self.__clients[gid]["cSt"] = st
      self.__clients[gid]["cEd"] = ed
      return True
    else:
      return False


  # method - A voice client closing time info get
  def getVCliClose(self, gid: int):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      return [self.__clients[gid]["cEn"], self.__clients[gid]["cSt"], self.__clients[gid]["cEd"]]
    else:
      return None


  # method - A voice client playing current music name
  def getVCliCurMusic(self, gid: int):
    # If specified guild_id's voice client is exist
    if self.__clients.get(gid) != None:
      return self.__clients[gid]["mCur"]
    else:
      return None


  # method - Closing music path get
  def getCloseMusic(self):
    return self.__mClose


  # method - Skip current playing music
  def skipMusic(self, gid: int):
    if self.__clients.get(gid) != None:
      self.__clients[gid]["vCli"].stop()
      return True
    else:
      return False


  # function - Check now is closing time
  def __isCloseTime(self, cst: time, ced: time):
    # Get current time in jp (+09:00)
    tnw_ut = datetime.now(timezone.utc)
    tnw_jp = tnw_ut + timedelta(hours=9)
    tnw = time(tnw_jp.hour, tnw_jp.minute)
    # Check
    if cst == ced:
      # If specified time is same
      return False
    elif cst < ced:
      # If start time is faster than end time
      if cst < tnw and tnw < ced:
        return True
      else:
        return False
    else:
      # If not
      if cst < tnw or tnw < ced:
        return True
      else:
        return False


  # method - Play trigger
  def trigPlay(self, arg1, arg2):
    # Loop each clients
    for cgid in self.__clients:
      # If not playing
      if not self.__clients[cgid]["vCli"].is_playing():
        # Set next music
        if self.__clients[cgid]["cEn"] and self.__isCloseTime(self.__clients[cgid]["cSt"], self.__clients[cgid]["cEd"]) and self.__mClose != "":
          self.__clients[cgid]["mCur"] = self.__mClose
        else:
          self.__clients[cgid]["mCur"] = self.__mList[randint(0, len(self.__mList) - 1)]
        # Try to play
        try:
          pObj = discord.FFmpegPCMAudio(self.__clients[cgid]["mCur"])
          pObj = discord.PCMVolumeTransformer(pObj, volume=self.__clients[cgid]["mVol"])
          self.__clients[cgid]["vCli"].play(pObj)
        except:
          self.__clients.pop()
          print("A voice client lost because of something went wrong. Count: %d" % len(self.__clients))
    return
