# Color-Swtich-Python-Game
This is a coding game project I created in my Introduction to Algorithms Course in Python.
This game is inspired by the IOS game called color switch found in the apple app store. 

In the demo video called "ActualColorSwithApp.MP4" you can see the idea of how the game works.

I used the graphic and basic idea of the game and tweaked it a little for a unique factor.
Instead of tapping enlessly to gain as many points as possible as in in the original game. I created a 30 point end goal to win the entire game. In the original game a the shape run at the sane speed. In my implemetation I striclty kept to a circle shape and made the circles spin faster as the game progresses. 

Given a file called Draw.py it allowed the vison I created apeear on a a canvas in a new window as a drawing.

The core functions of the game lies in the file called ColorSwitch.py.
initializeTargets():
	#create the target list that will have:
	#donuts(rotating circles) & bullseyes(color changeing ball)
  def targetOverlaps(target, yTop):
  def drawDonut(target, yTop):
  def drawBullsEye(target, yTop):
  def drawBoard(targets, ballY, ballColor, yTop, score): 
  def rotateDonuts(targets): 
  def bottomColor(target): 
  def topColor(target):
  def ballDied(targets, ballY, ballColor):
  def ballHitBullseye(targets, ballY): 
  def ballHitStar(targets, ballY, score): 
  def getYtop(bally):
  def playGame(targets):
  def loseWin(loseWin, xS, score, y1C, y2C):
To the run the file it is vital to dowload all the file to one folder so the class oject Draw file and graphics ending in ".gif" can seamlessy display the game to the client. 
