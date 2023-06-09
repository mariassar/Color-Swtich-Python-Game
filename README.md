# Color-Swtich-Python-Game
This game is inspired by the iOS app called "Color Switch" found in the Apple App Store. In the demo video called "ActualColorSwitchApp.MP4," it displays the basic idea of how this game works.

In this implementation, the graphics and basic idea of the original game are utilized, aside from some minor aspects that allow for a uniqueness factor. Instead of tapping endlessly to gain as many points as possible, as in the original game, this game has a 30-point end goal to win the entire game. Additionally, in the original game, every shape runs at the same speed. In this implementation, only a circle shape is utilized, and each new circle on the screen runs at a faster speed as the game progresses.
The file called Draw.py allows this inspired vision to appear on a canvas in a new window as a drawing. 

The core functions of this game lie in the file called ColorSwitch.py. The main two "shapes" or targets to keep track of within the game are the rotating circles along that are connected to the color changning "bullseye" (as ilustrated in the file called "Bull.gif") along with star that ups the score counter(as ilustrated in the file called "Star.gif") , and the other traget whcih is the the random color-changing ball.

The most challenging concept to solve was figuring out which coordinates of each target should be displayed on the canvas at any given moment of the running game. This challenge was resolved by creating and drawing a long list of targets along with their y coordinates and increasing their coordinates so they would match that of the canvas window and could therefore be displayed to the client. The challenge I enjoyed the most was figuring out the math for the circle created with 4 colors and being able to keep track of where each color is within each circle as they each rotate. The planning and concepts of these challenges are illustrated in the demo diagrams labeled "ColorSwitchWhiteboardDiagrams.pdf."

Once every function was set up, the function playGame() was created to compile all the functions together to have them work seamlessly into the function called loseWin() which take the graphic files called "Confetti.gif" and "ColorSwitchLogo.gif" to notify the client if they have won or lost. To run the file, it is vital to download all the files to one folder so that the class object Draw file and graphics ending in ".gif" can seamlessly display the ColorSwitch.py game to the client.
