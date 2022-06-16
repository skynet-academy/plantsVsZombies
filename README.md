# Plants vs Zombies

## Description:

Plants vs Zombies is a game made purely in python, it requires the basic
understanding of object oriented programming. 

Plants vs Zombies: version 0.1

## Summary:

1. Operating systems where it can be run.
2. Installation
3. How to play it.
4. Video game's tree structure.

### 1. Operating systems where it can be run.

- Windows, Linux

### 2. Installation:

1. Installing Python:
    - On Ubuntu/Debian base:
        - ```sudo apt-get install python3```
    - On Windows:
        - download the binaries <a href="https://www.python.org/downloads/">
          here</a> and follow the instructions.

2. Installing pip:
    Once you have python, download the pip file by writting the following command in the
terminal.
    - ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```.
    
    then, after downloading the pip file, execute it using python.
    - On Linux/MacOs:
        - ```python3 -m pip --version```.
    - On Windows:
        - ```python.exe -m pip --version```.
3. Installing all packages to run "arcade" library.
    Once we have python and pip, we continue with arcade library.
    - ```pip install -r requirements.txt```

### 3 .How to play it.

if you are in Linux or MacOs:
    - ```python3 game.py```
if you are in Windows:
    - ```python.exe game.py```

### 4. Video game's tree structure.

```
  |---- PlantsVsZombies
  |-----------|
  |           |---- assets
  |           |        |---- images
  |           |        |---- __init__.py
  |           |        |---- sounds
  |           |
  |           |---- utilities
  |           |         |---- collisions.py
  |           |         |---- eating_plants.py
  |           |         |---- __init__.py
  |           |         |---- plant_position.py
  |           |
  |           |---- charactes
  |           |         |---- buckhead_zombie.py
  |           |         |---- conehead_zombie.py
  |           |         |---- ordinary_zombie.py
  |           |         |---- pea.py
  |           |         |---- peashoter.py
  |           |         |---- sunflower.py
  |           |         |---- sun.py
  |           |         |---- torchwood.py
  |           |         |---- wallnut.py
  |           |         |---- zombie.py
  |           |         |---- __init__.py
  |           |
  |           |---- __init__.py
  |           |
  |           |---- game.py
  |           |
  |           |---- README.md
  |           |
  |           |---- settings.py
  |           |
  |           |---- requirements.txt
```



