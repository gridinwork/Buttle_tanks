# Buttle_tanks — Tank Battle Solo Test v0.2

Windows/Python recreation inspired by classic 8-bit tank battle gameplay.

## Current version

**v0.2 — first public project version**

Default mode is **single-player level progression**.

### Features

- 12 playable levels;
- enemy AI with progressive spawning;
- score and player lives;
- defendable base;
- destructible brick walls;
- steel, water, forest and ice terrain;
- shot, hit, explosion, level-start and game-over audio;
- automatic transition to the next level;
- fullscreen mode;
- optional cooperative launcher and experimental AI/API modules.

## Controls

- **Arrow keys** — move
- **Space** or **Enter** — fire
- **F11** — fullscreen
- **Esc** — pause/menu
- **R** — restart after Game Over

## Run on Windows

The easiest way is to launch:

```bat
start.bat
```

The launcher installs `pygame-ce` if needed and starts the game.

Manual launch:

```bash
pip install -r requirements.txt
python game.py
```

## Build Windows EXE

Run:

```bat
build_exe.bat
```

## Assets

Graphics are loaded from `Dump.nes` when available. If it is missing, built-in fallback sprites are used.

Audio files are stored in the `audio/` directory.

## Project status

This repository contains the first uploaded development version. The game will continue to be updated in later versions.
