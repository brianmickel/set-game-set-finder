# SET(c) Game Set Finder

## General Flow
1. Input Cards present on Table
1. Interface informs User if a set exists but doesn't say which set
1. User interaction to learn the sets

## Project Stages
1. CLI Interface to Input Cards
1. Web interaction (all frontend?)
1. Image upload to website
1. mobile app real time image like bank check deposit

1. n-dimensional set (Cards have 4 characteristics with three options each -> sets of 3 => number of cards to make a set equals number of options)

## Solver Types
1. for every pair on table -> check if third item also on table
1. enumerate all sets of three on table -> check if set for each
1. can I design a way to hash the cards on the table that would go true or false but not tell the set (this would have no way to leak info to user, maybe, does it matter?)
1. 

## To Do
* TODO Add testing (turn the comments into tests)
* TODO clean up comments in code
* TODO more forgiving import? csv? how should data enter the system
* look into https://en.wikipedia.org/wiki/Doctest
* write out the different types of solvers
* ideate on interaction for CLI
** does it display instructions but not options?
** does it display all options and you select highlight then with arrows keys and keyboard input?
* decide language(s) for project
* make a gif for each project stage
* make a gif for evolution of project
* find/make better card images
* explore what it'd take to make a n-dim set game
** how do different solver types scale?

## Future Projects
* Set Game like the NY Times one
* Set card generator


Similar Projects / Inspiration / Links
* https://github.com/jgrodziski/set-game (*****)
* https://github.com/welefen/SetCard (*?)
* https://github.com/SleekPanther/set-game (*?)
* https://github.com/hildjj/set-game (*?)
* https://github.com/henrikw/SetGame/blob/master/src/SetGame.java (*?)
* https://github.com/tomwhite/set-game (*****)

## IMPORTANT COPYRIGHT
* SET is Copyright, this is for educational purposes only
