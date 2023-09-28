# Min-Max Connect4 #

**Name:** Connect4  
**Version:** 0.1

A graphic based connect 4 game which implements the Min-Max algorithm to determine the computer player's best available move.

I use the pygame Python library to make the graphic interface version of the game and run multiple simulations of games between computers using the Min-Max algorithm to make their moves and gather different statistics from it.

## To play ##

First, be sure to clone the repository
```
git clone https://github.com/Notgard/min_max_connect4.git
```

Afterwards, head into the cloned repository and install dependencies.
(Make sure to have python and pip installed)
```
cd MinMax-Connect4/
pip install -r requirements.txt
cd /src
python3 main.py
```
## Changelog ##

### 0.2 ###
TODO:
* Switch between different modes (player vs computer, player vs player, computer vs computer)
* Run game simulations on different processes
* Collect statistics from ran simulations
* Generate human readable charts of stats

### 0.1 ###
* Singleplayer connect4 graphic interface with min-max computer moves available
