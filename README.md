# Color-Swtich-Python-Game
This is a coding game project I created in my Introduction to Algorithms Course in Python.
This game is inspired by the IOS game called color switch found in the apple app store. 

In the demo video called "ActualColorSwithApp.MP4" you can see the idea of how the game works.

I used the graphic and basic idea of the game and tweaked it a little for a unique factor.
Instead of tapping enlessly to gain as many points as possible as in in the original game. I created a 30 point end goal to win the entire game. In the original game a the shape run at the sane speed. In my implemetation I striclty kept to a circle shape and made the circles spin faster as the game progresses. 

Given a file called Draw.py it allowed the vison I created apeear on a a canvas in a new window as a drawing.

The core functions of the game lies in the file called ColorSwitch.py.
The main two shapeesor targets to keep track of were the rotateing cricles and color changing ball.

The most challengign concpet to impelment was to know whichc cordinates of the targets should be displayed on the canvas at any givem moement. This chellege was resolved by created a long list of targets and their y cordinate to be created prior to the game and hs the color changing ball's y cordinate increaced the y corrdinate of the target list would be displayed on the canvas.

The challge I enjoyed the most was figuring out the mtah for the circle created 4 colors ebing able to keep track where each color is within each circle as they each roatate.

The planning and concepts of these challehnging are ilustrated in the file demos labled "ColorSwitchWhiteboardDiagrams.pdf"

Once everythign was set up thee function playGame() drievs the entire file to create the seamless final output game of Color Switch.py.

To the run the file it is vital to dowload all the file to one folder so the class oject Draw file and graphics ending in ".gif" can seamlessy display the game to the client. 
