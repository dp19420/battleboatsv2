## Battledingy Game

A simple Battledingy( small ships with no ability to fire back, pirates with small arms in speedboats basicly) game implemented in Python and deployed on Heroku.

### Features

- 10x10 grid for the game board
- Random placement of 7 single location ships on the computer's grid
- Input validation for row and column coordinates
- Tracking of hit and miss shots on the player's grid
- Countdown of remaining turns

### How to play

1. The game will randomly place 7 ships on a 10x10 grid.
2. Enter row and column numbers to fire shots.
3. Try to sink all 7 ships before running out of turns.

### Running the Game

The Game is deployd on Heroku at:["Heroku"](https://dashboard.heroku.com/apps/battleboat/deploy/github)

### Code

The code for the game is contained in the run.py file, which is deployed on Heroku.

- target_grid and aim_grid represent the computer's and player's grids.
- print_grid(grid) prints the given grid.
- place_ships(grid) randomly places ships on the grid.
- place_shot() prompts the user for row and column coordinates.
- sunk_ships(grid) counts the number of ships on the grid.
The main loop runs until the player wins or loses.

### Testing

- Have run it through a PEP8 validator
- Tried wrong input (both strings and to high numbers)
- Tested in gitpd terminal and Heroku

#### Validator result
 - PEP8
     - No warnings


### Deployment

Deployed to Heroku

### Further plans

- Currently this is a offensive game and i wish to add the abbility for the computer to fire back and for the player to place his own ships.
- Size settings for the grid currently abandond becouse i could not figure out a clean way of doing it in time. Might work more on that later.  

### Credits

- Love sandwiches walktrough, without that i would still not have been anywhere.