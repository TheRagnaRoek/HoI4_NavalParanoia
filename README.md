# HoI4 - Naval Paranoia
This is a short script for those HoI4 players that don't feel like they're
hearing the ear-caressing harmony of the naval invasion sound enough in
their games. The program will randomly play the ever so beloved naval invasion sound from the game
Hearts of Iron 4 in time intervals between 5 to 120 seconds.

## Requirements
This program requires Python version 3.8 or higher to be used. <br>
It also requires the 3rd party library "PyAudio" (programmed using Version 0.2.14).

## How to Use
Keep "naval_paranoia.py" and "naval_invasion.wave" in the same folder for proper function.
Using the command line, start the script by entering: <br>
`python naval_paranoia.py` <br>

This will start the program with the standard naval invasion sound. If you want to use a custom sound,
either put the soundfile into the same folder as the script and enter: <br>
`python naval_paranoia.py filename.wav` <br>

or directly refer to the soundfile by putting the filepath into the command line like this: <br>
`python naval_paranoia.py filepath/filename.wav`

## Upcoming Updates
- add option to customise time interval through command line
- add a command line user interface for ease of use

## Credits

"Hearts of Iron 4" and its associated trademarks are the protected property of
Paradox Interactive AB, Sweden. This includes the sound file used
in this program (naval_invasion.wave), which is not used with the intention to infringe on
said copyright. <br>
https://www.paradoxinteractive.com/our-games/all-games?amount=20&Brand=Hearts%20of%20Iron

PyAudio 0.2.14 by Hubert Pham. https://pypi.org/project/PyAudio/

Credits to Reddit user u/Markilgrande for the idea.

Program by TheRagnaRoek aka Dennis Ragnar van Reem <br>
Last Updated: December 2024
