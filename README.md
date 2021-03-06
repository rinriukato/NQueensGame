# 8 Queens Game

## Preface

Personal python project. Made in a day.
If you don't know what the 8 queens problem is, [here it is](https://en.wikipedia.org/wiki/Eight_queens_puzzle).

This is not a preset of placed queens, and therefore is not a backtracking solution. You as the player place down the pieces and it checks if you managed to complete the puzzle.
This was just a personal project I wanted to make and experiment in making GUIs in Python. 

## Features
* Utilizes the pygame library in order to make the GUI. 
* Requires all 8 queens in order to finish the game
* Has a neat red warning line showing you where there is a conflict

## Issues
* Diagonal error marking is not working as expected. Fix later
* Executable version has issues, reports not having the python? library. Fix later

## How to run
* Have python3 and the pygame library on your machine and execute via ```python3 queensGUI.py```

## Notes
The first file, 'sneakyQueens.py' is a basic solution to solving the nQueens problem as mentioned above. In this case it has the restriant of a premade board in order to simulate input but should work with boards of any size. I wanted to mess around with GUIS so I decided to work on a simple and old class project and extend upon it to make it a lot cooler.
