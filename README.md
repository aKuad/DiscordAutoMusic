# DiscordAutoMusic

## Description

This is discord music play bot program.

It supported for local storage's sound files playing.
Not supported for online streaming (example: youtube, soundcloud).

The music to play will selected in random. (Except closing time music.)
Users manually music selecting is not supported.

## Note

This program using `discord.py`, an API wrapper of discord.
But `discord.py` is already stopped development and maintaining.

Using this program with `discord.py`, there is a possibility of security incident or bug occur.
But I will not take any liability or warranty.
Please use it with self-liability.

## Bot control command

### Useage

> `!ncs <sub command>`

All commands except 'help' require user's voice connection.

`!ncs` is default prefix. (I started development it because of NCS music playing. So I specify the prefix because of the reason.)

If you want change it, please modify line 64 in `main.py`.

> if com[0] != "!ncs":

(However, the help message does not change automatically.)

### Sub commands

```txt
h           , help            Print this help
c [vol]     , connect [vol]   Connect and start music playing
                              (with setting volume to [vol])
p [vol]     , play [vol]        (same as `c`)
dc          , disconnect      Stop music playing and disconnect
st          , stop              (same as `dc`)
sk          , skip            Skip and play next music
v [vol]     , volume [vol]    Print current volume or set volume to [vol]
                              (accept from next music)
i           , info            Print current music information
cl [st] [ed], close [st] [ed] Print current closed time or set closed time
r [st] [ed] , rest [st] [ed]    (same as `cl`)
```

### About closing time

Between the time [st] to [ed], music will be play only closing music.
Argument format of [st] [ed] is `HH:MM`.

> example: `!ncs cl 1:00 7:00`

To disable closing time, specify same time.

> example: `!ncs cl 0:00 0:00`

## How to run

### 1. Additional packages installation

This program is using some python additional packages.

To install these packages:

```sh
pip install discord.py[voice] pyexifinfo
```

### 2. Make `conf.json`

Please copy `conf_sample.json` to `conf.json` and edit.

The json file has these config.

* `token` (Required)
  * Specify your discord bot token.
* `music_dir` (Required)
  * Specify sound file(s) path for normal music.
  * Using wildcard `*` or specify directory, you can specify multiple files.
* `music_close` (Optional)
  * Specify sound file path for closing music.
  * It option can specify only single file.
  * If it specified `""` (nothing), closing-time function will be disabled.
  * It is optional, but do not remove the key. If removed, key error will be occur.

### 3. Run

Please execute `main.py` with python interpreter.

```sh
python main.py
```
