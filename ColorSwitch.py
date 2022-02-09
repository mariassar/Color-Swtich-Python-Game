#Color Switch Game: Mariassa Royzenberg : CS 1300: 2021
import Draw, math, random

#To Win: go through all 30 circles as the speed gets faster and faster

#Colors
Yellow = Draw.color(250, 255, 0)
Purple = Draw.color(144, 13, 255)
SkyBlue = Draw.color(50, 219, 240)
HotPink = Draw.color(255, 1, 129)
	
def initializeTargets():
	#create the target list that will have:
	#donuts(rotating circles) & bullseyes(color changeing ball)
	targets = []
	
	#variables
	yCoord = 90
	angle = 0
	speed = 11
	starVisible = True
	bullseyeVisible = True
	
	#the most the yCoord can be for the last circle in the target list
	yMost = 10400 

	#while the yCoord is less than yMost 
	while yCoord < yMost:
		#each donut has a diffrent y coordinate, size, and speed
		size = random.randint(150, 200)
		radiusBig = int(size / 2)
		speed -= .25
		donut = ["donut", yCoord, angle, size, speed, starVisible]
		targets += [donut]
		#each bullseye has diffrent y coordinate
		yCoord += radiusBig + 200
		bullseye = ["bullseye", yCoord, bullseyeVisible]
		targets += [bullseye]
		yCoord += 150
		size = random.randint(150, 200)
		radiusBig = int(size / 2)
		speed -= .25
		donut = ["donut", yCoord, angle, size, speed, starVisible]
		targets += [donut]		
		yCoord += radiusBig + 200
		
	return targets

def targetOverlaps(target, yTop):
	#how many pixels from the top of the screen to the bottom
	screenHeight = 680
	
	#if either bottom donut above yTop or top donut below yTop+screenHeight
	if target[0] == "donut" and target[3] + target[1] < yTop or \
	   target[1] > yTop + screenHeight: 
		return False
	
	#if either bottom bullseye above yTop or top bullseye below yTop+screenHeight
	if target[0] == "bullseye" and target[1] + 50 < yTop or \
	   target[1] > yTop + screenHeight: 
		return False
	
	return True

def drawQaurterFilledCircle(x, y, wide, startAngle, endAngle):
	#variables
	x = x + wide / 2
	y = y + wide / 2    
	coords = [x, y] 
	
	#create the quarter by drawing line segments
	for angle in range(startAngle, endAngle, 5):
		rad = math.radians(angle)
		newx = math.cos(rad) * wide / 2
		newy = math.sin(rad) * wide / 2
		coords += [x + newx, y - newy]  
		
	#draw quarter
	Draw.filledPolygon(coords)

def drawDonut(target, yTop):
	#donut = ["donut", yCoord, angle, size, speed, starVisible]
	#draw donut using quarter circles w/ diffrent start & end angles and colors
	donut = target
	radiusBig = donut[3] / 2
	radiusSmall = (radiusBig) - 15	
	
	#subtract yTop from every yCoord to allow it to be in the vewing window
	Draw.setColor(Yellow)
	drawQaurterFilledCircle(190 - radiusBig, donut[1] - yTop, donut[3], \
				donut[2], 91 + donut[2])
	Draw.setColor(HotPink)
	drawQaurterFilledCircle(190 - radiusBig, donut[1] - yTop, donut[3], \
				90 + donut[2], 181 + donut[2])
	Draw.setColor(SkyBlue)
	drawQaurterFilledCircle(190 - radiusBig, donut[1] - yTop, donut[3], \
				180 + donut[2], 271 + donut[2])
	Draw.setColor(Purple)
	drawQaurterFilledCircle(190 - radiusBig, donut[1] - yTop, donut[3], \
				270 + donut[2], 361 + donut[2])  
	Draw.setColor(Draw.BLACK)        
	Draw.filledOval(190 - radiusSmall, donut[1] - yTop + 15, donut[3] - 30, \
			donut[3] - 30)
	
	#if the star is visible 
	if donut[5]:
		#draw the star
		Draw.picture("Star.gif", 160, radiusSmall + (donut[1] - yTop - 20))

def drawBullsEye(target, yTop):
	#bullseye = ["bullseye", yCoord, bullseyeVisible]
	bullseye = target
	
	#subtract yTop from yCoord to allow it to be in the viewng window
	#if the bullseye is visible
	if bullseye[2]:
		#draw the bullseye
		Draw.picture("Bull.gif", 165, bullseye[1] - yTop)
		
def drawBoard(targets, ballY, ballColor, yTop, score): 
	#clear the canvas
	Draw.clear()
	
	#for each target in the target list	
	for target in targets: 
		#if the target overlaps the veiwing window
		if targetOverlaps(target, yTop):
			#if the target is a donut
			if target[0] == "donut":
				#draw the donut
				drawDonut(target, yTop)
			else:
				#otherwise draw a bullseye
				drawBullsEye(target, yTop)
	
	#draw the logo near the bottom of strip of circles
	Draw.picture("ColorSwitchLogo.gif", 45, 11000 - yTop)
	
	#draw the user ball
	Draw.setColor(ballColor)
	Draw.filledOval(180, ballY - yTop, 20, 20) 
	
	#draw the score
	Draw.setColor(Draw.WHITE)
	Draw.setFontFamily("Times New Roman")
	Draw.setFontBold(True)
	Draw.setFontSize(50)
	Draw.string(str(score), 20, 20)
	
	#show the canvas
	Draw.show(30)

def rotateDonuts(targets): 
	#for each target in the list of targets
	for target in targets:
		#if the target is a donut
		if target[0] == "donut":
			#increment it's angle by the int of the speed
			target[2] += int(target[4])
	
def bottomColor(target): 
	#remove extra 360's from angle
	angle = target[2] % 360
	
	#find bottom color based on where the angle is
	if angle >= 0 and angle <= 90:
		bottomColor = SkyBlue
	if angle >= 91 and angle <= 180:
		bottomColor = HotPink
	if angle >= 181 and angle <= 270:
		bottomColor = Yellow
	if angle >= 271 and angle < 361:
		bottomColor = Purple
		
	#return the color that is currently at the bottom of that donut
	return bottomColor
	
def topColor(target):
	#remove extra 360's from angle
	angle = target[2] % 360
	
	#find bottom color based on where the angle is
	if angle >= 0 and angle <= 90:
		topColor = Yellow
	if angle >= 91 and angle <= 180:
		topColor = Purple
	if angle >= 181 and angle <= 270:
		topColor = SkyBlue
	if angle >= 271 and angle < 361:
		topColor = HotPink
		
	#return color that is currently at the top of that donut	
	return topColor
	
def ballDied(targets, ballY, ballColor):
	#for each target in the  list of targets
	for target in targets:
		
		#if the target is a donut
		if target[0] == "donut":	
			radiusBig = target[3] / 2
			
			#if ballY is anywhere within wedge of bottom of the donut	
			if ballY >= target[1] + target[3] - 15 and \
			   ballY <= target[1] + target[3]:
				
				#get the bottomColor of the current donut
				bottomColor(target)
				
				#if the bottom color is different than ballColor
				if bottomColor(target) != ballColor:
					return True
				return False
			
			#if ballY is anywhere within wedge of top of the donut
			if ballY >= target[1] and ballY <= target[1] + 15:
				
				#get the topColor of the current donut
				topColor(target)
				
				#if the topColor is different than ballColor
				if topColor(target) != ballColor:
					return True
				return False

def ballHitBullseye(targets, ballY): 
	#for each target in the list of targets
	for target in targets:
		
		#if the target is a bullseye and the bullseye is visible
		if target[0] == "bullseye" and target[2]:
			
			#if ballY is within bullseyes yCoords from top to bottom
			if ballY >= target[1] - 10 and ballY <= target[1] + 30:
				
				#make the bullseye not visible
				target[2] = False
				return True
	return False

def ballHitStar(targets, ballY, score): 
	#for each target in the list of targets
	for target in targets:
		
		#if the target is a donut and the star is visible
		if target[0] == "donut" and target[5]:
			radiusBig = target[3] / 2
			
			#if ballY is within the stars yCoords from top to bottom
			if ballY >= radiusBig + target[1] - 20 and \
			   ballY <= radiusBig + target[1]:
				
				#make the star not visible
				target[5] = False
				return True
	return False

def getYtop(bally):
	#get yTop
	return bally - 400

def playGame(targets):
	#initialiy this is a large Y near the bottom of the "strip" of circles
	ballY = 11000
	
	#initially this also a large Y near the bottom of the "strip" of circles
	yTop = getYtop(ballY)
	
	#initialize ballColor
	ballColor = random.choice([SkyBlue, HotPink, Yellow, Purple])
	
	#initialize score
	score = 0
	
	#initialize bounce varibles
	bounceSize = 8
	bounce = 10
	bounceDir = -1
	fuel = 0
	
	#play game if ballY is greater than 0
	while ballY > 0:
		
		#if the user pressed a key
		if Draw.hasNextKeyTyped():
			#get the key
			key=Draw.nextKeyTyped()
			if key == 'space':
				fuel += 10
		
		#bouncing ball
		if fuel > 0:
			ballY -= 10
			yTop = getYtop(ballY)
			fuel -= 4
			if fuel == 0:
				bounce = bounceSize // 2
				bounceDir = -1
		else:
			ballY += (bounceDir * 3)
			bounce += bounceDir
			if bounceDir == -1:
				if bounce == 0: 
					bounceDir = 1
			else:
				if bounce == bounceSize:
					bounceDir = -1
		#rotate the donuts
		rotateDonuts(targets)
		
		#if ball died then return the score 
		if ballDied(targets, ballY, ballColor):
			return score
		
		#if the ball hit the bullsye randomly select a new color
		if ballHitBullseye(targets, ballY):
			if ballColor == SkyBlue:
				ballColor = random.choice([HotPink, Yellow, Purple])
			elif ballColor == HotPink:
				ballColor = random.choice([SkyBlue, Yellow, Purple])
			elif ballColor == Yellow:
				ballColor = random.choice([SkyBlue, HotPink, Purple])
			else: 
				ballColor = random.choice([SkyBlue, HotPink, Yellow])			
				
		#if the ball hit a star 
		if ballHitStar(targets, ballY, score): 
			#increment score	
			score += 1
		
		#draw the board
		drawBoard(targets, ballY, ballColor, yTop, score)
			
	return score
	
def loseWin(loseWin, xS, score, y1C, y2C):
	#clear the canvas
	Draw.clear()
	
	#confetti for winning screen
	Draw.picture("Confetti.gif", 0, y1C)
	Draw.picture("Confetti.gif", 0, y2C)
	
	#color switch logo
	Draw.picture("ColorSwitchLogo.gif", 40, 190)
	Draw.setColor(HotPink)
	
	#lose or win text
	Draw.setFontFamily("Times New Roman")
	Draw.setFontBold(True)
	Draw.setFontSize(50)
	Draw.string(loseWin, xS, 170)	
	
	#your score .. is text
	Draw.setColor(SkyBlue)
	Draw.setFontBold(False)
	Draw.setFontSize(30)	
	Draw.string("Your score is: ", 90, 360)
	Draw.setColor(Draw.WHITE)
	Draw.string(str(score), 265, 360)	
	
	#show the canvas
	Draw.show()	
	
def main():
	#draw the canvas
	Draw.setCanvasSize(380, 680)
	Draw.setBackground(Draw.BLACK)
	
	#return a list of targets
	targets = initializeTargets() 
	
	#play the game
	score = playGame(targets)
	
	#play lose or win screen depending on score
	if score == 30:
		loseWin("You Won!", 80 , score, 0, 550)
	else:
		loseWin("Game Over", 70, score, 680, 680)		
main()

              




    
    




