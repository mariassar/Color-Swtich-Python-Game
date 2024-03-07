# Color-Swtich-Python-Game
This game is inspired by the iOS app called 'Color Switch,' which can be found in the Apple App Store. In the demo video file called "ActualColorSwitchApp.MP4," it displays the basic idea of how this game works.

In my implementation, the graphics and basic idea of the original game are utilized, aside from some minor tweaks that allow for a uniqueness factor. For instance, instead of tapping endlessly to gain as many points as possible, as in the original game, my version of the game has a 30-point end goal to win the entire game. 
Additionally, in the original game, every shape runs at the same speed. In this implementation, only a circle shape is utilized, and each new circle on the screen runs at a faster speed then the previous, as the game progresses.
The file called "Draw.py" allows this inspired vision to appear on a canvas in a new window as a drawing. 

The core functions of this game lie in the file called "ColorSwitch.py". 

The main two 'shapes' or targets to keep track of within the game are the 'rotating circles' that are connected to the star shape that ups the score counter (this target's graphic symbol is illustrated in the file called "Star.gif"); as well as the 'bullseyes' that allows for the users ball to change to a random color when passed (this target's graphic symbol is illustrated in the file called "Bull.gif").

The most challenging concept to be solved, in the creation of this vision, was in firguring out which y coordinates of each target should be displayed on the canvas at any given moment of the running game. This challenge was resolved by creating and drawing a long list of targets (prior to the start of the game) along with their y coordinates, and further decreasing these coordinates so they would match that of the canvas window, and could therefore be displayed to the user. 
The challenge I enjoyed the most was figuring out the math behind the four-color-quartered circle (this is displayed in the function called drawQaurterFilledCircle()). It involved keeping track of the radians for each quarter angle, in order for the program to be able to determine when the users ball y-coordinate was touching a specific color on the circle. This calculation allowed the program to identify the color even as the circle rotated. The planning and soultions toward these challenges are illustrated in the drawings labeled "ColorSwitchWhiteboardDiagrams.pdf."

When this game is run, the function playGame() compiles all the functions together to have them work seamlessly. When the game ends the score is returned and then outputed into the function called loseWin() which take the graphic files called "Confetti.gif" and "ColorSwitchLogo.gif" to display to the user if they have won or lost, as well as their final score. 

To run this game, it is vital to download all the files to one folder so that the class object Draw file and graphics ending in ".gif" can seamlessly display the ColorSwitch.py game to the user.
