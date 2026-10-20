# DragonShoot

DragonShoot is a small 2D space-shooter game built with Python and Raylib. Pilot a ship, dodge incoming meteors, and shoot them down for as long as you can. Based on a tutorial by Clear Code. I only changed the theme/design of the game.
<img width="1270" height="614" alt="image" src="https://github.com/user-attachments/assets/aab35aaa-20b9-4369-ae36-3f1e12b91f3e" />

## Features

- Keyboard-controlled movement and laser fire
- Meteors that spawn continuously and move at varying speeds
- Collision detection, explosion animations, and sound effects
- A survival-time score

## Requirements

- Python 3
- The `raylib` Python package, which provides the `pyray` and `raylib` modules used by the game
- The game assets listed below

Install the dependency with:

```bash
python -m pip install raylib
```

## Assets

The game loads its images, sounds, and font from an `audio` directory one level above the current working directory. This asset directory is not included in this repository. Before starting the game, provide these files in that location:

```text
audio/
├── spaceship.png
├── star.png
├── laser.png
├── meteor.png
├── laser.wav
├── explosion.wav
├── music.wav
├── Stormfaze.otf
└── explosion/
    ├── 1.png
    ├── 2.png
    └── ...  # through 28.png
```

For example, if the repository is at `C:\games\DragonShoot`, the assets must be at `C:\games\audio`. Run the game from the repository directory so the relative asset paths resolve correctly.

## Run the game

From the repository directory, run:

```bash
python main.py
```

`game2d.py` is also an executable game entry point.

## Controls and gameplay

| Key | Action |
| --- | --- |
| Arrow keys | Move the ship |
| Space | Fire a laser |
| Esc or close the window | Exit |

Survive as long as possible and shoot meteors before they hit your ship. The score shows elapsed time in seconds.

## Help

For problems with the game or setup, open an issue on the repository's hosting page and include your operating system, Python version, and any error message.

## Contributing and maintenance

Contributions are welcome. Fork the repository, make a focused change, and open a pull request describing what changed and how you checked it. This repository does not currently include a separate contribution guide or automated test suite.

No maintainer contact or license file is included in the repository; check the repository hosting page for current ownership and licensing information.
