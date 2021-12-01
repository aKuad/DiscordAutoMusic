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
    self.__mList = self.__mList.stdout.decode("UTF-8").split("\n")
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
  def getVCliCloseMusic(self):
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
    tnw_ut = datetime.now(timezone.utc)
    tnw_jp = tnw_ut + timedelta(hours=9)
    tnw = time(tnw_jp.hour, tnw_jp.minute)
    if cst == ced:
      return False
    elif cst < ced:
      if cst < tnw and tnw < ced:
        return True
      else:
        return False
    else:
      if cst < tnw or tnw < ced:
        return True
      else:
        return False


  # method - Play trigger
  def trigPlay(self, arg1, arg2):
    for cCli in self.__clients.values():
      if not cCli["vCli"].is_playing():
        if cCli["cEn"] and self.__isCloseTime(cCli["cSt"], cCli["cEd"]) and self.__mClose != "":
          cCli["mCur"] = self.__mClose
        else:
          cCli["mCur"] = self.__mList[randint(0, len(self.__mList) - 1)]
        pObj = discord.FFmpegPCMAudio(cCli["mCur"])
        pObj = discord.PCMVolumeTransformer(pObj, volume=cCli["mVol"])
        cCli["vCli"].play(pObj)
    return
