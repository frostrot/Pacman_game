import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,0.1)
RIGHT = (0.1,0)
TOP = (0,-0.1)
LEFT = (-0.1,0)
stop = (0,0)
state = 3
lives=3

#Draws a rectangle for the wall and skip position where i am displaying score
def draw_wall(screen, pos):
	if(pos != (0,0) and pos != (1,0) and pos != (2,0) and pos != (3,0) and pos != (4,0) and pos != (5,0) and pos != (6,0) and pos != (7,0) and pos!=(17,15) and pos!=(18,15) and pos!=(19,15)):
		pixels = pixels_from_points(pos)
		image = pygame.image.load('output-onlinepngtools.png')
		screen.blit(image,pixels)

'''Draws a rectangle for the player and drawpacman
and what not everything is here but you cant see and yes enemies also, yes still didnt caught
add_to_pos ; screen display ; and then intitialization'''

def draw_pacman(screen, pos,coincount1,move_direction,state): 
	pixels = pixels_from_points(pos)
	if(move_direction==LEFT):
		#loading image onto the screen and bliting them
		image = [pygame.image.load('lpac1.png'),pygame.image.load('lpac2.png')]	
		screen.blit(image[coincount1//8],pixels)
	elif(move_direction==RIGHT):
		image = [pygame.image.load('rpac1.png'),pygame.image.load('rpac2.png')]	
		screen.blit(image[coincount1//8],pixels)
	elif(move_direction==TOP):
		image = [pygame.image.load('upac1.png'),pygame.image.load('upac2.png')]	
		screen.blit(image[coincount1//8],pixels)
	elif(move_direction==DOWN):
		image = [pygame.image.load('dpac1.png'),pygame.image.load('dpac2.png')]	
		screen.blit(image[coincount1//8],pixels)
	else:
		if state == 0:  # condition for different kind of image display
			image=[pygame.image.load('upac1.png'),pygame.image.load('upac2.png')]
			screen.blit(image[coincount1//8],pixels)
		elif state == 1:
			image=[pygame.image.load('dpac1.png'),pygame.image.load('dpac2.png')]
			screen.blit(image[coincount1//8],pixels)
		elif state == 2:
			image=[pygame.image.load('lpac1.png'),pygame.image.load('lpac2.png')]
			screen.blit(image[coincount1//8],pixels)
		elif state == 3:
			image=[pygame.image.load('rpac1.png'),pygame.image.load('rpac2.png')]
			screen.blit(image[coincount1//8],pixels)

''' Draw enemy and blit screen rectangle and what not 
	do whatever it is there i dont care.
	get my point or not orbit about the spin and skiping it all through'''

def draw_enemy(screen, pos,coincount2):
	pixels = pixels_from_points(pos)
	image = [pygame.image.load('ghost1.png') ,pygame.image.load('ghost2.png'),pygame.image.load('ghost3.png') ]
	screen.blit(image[coincount2],pixels)

def draw_lives(screen,pos):
		pixels = pixels_from_points(pos)
		image = pygame.image.load('lpac2.png')
		screen.blit(image,pixels)

#Draws a rectangle for the coin
def draw_coin(screen, pos,coincount):
	pixels = pixels_from_points(pos)
	image = [pygame.image.load('1-coin.png'),pygame.image.load('2-coin.png'),pygame.image.load('3-coin.png'),pygame.image.load('4-coin.png'),pygame.image.load('5-coin.png'),pygame.image.load('6-coin.png')]
	screen.blit(image[coincount],pixels)

#Uitlity functions
def add_to_pos(pos, pos2):
	return [pos[0]+pos2[0], pos[1]+pos2[1]]
def pixels_from_points(pos):
	return [pos[0]*WIDTH, pos[1]*HEIGHT]

#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((640,512), 0, 32)
background = pygame.surface.Surface((640,512)).convert()


#Initializing variables
'''Some thing to define the screen size ,pixel, dimension
pacman,enemy,walls, lauda and lahsun, coins of different
shape, time, clock and everything.'''

layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = coinp = [1,1]
coinposx = coinposy = 9
enemy1_position = [8.0,6.0]
e1_direction = RIGHT
enemy2_position = [9.0,6.0]
e2_direction = TOP
enemy3_position = [10,6]
e3_direction = LEFT
background.fill((255,255,255))
bg = pygame.image.load('index.jpeg')
coincount=score=coincount1=0
# Main game loop 
'''main game loop does all the movement and every
other thing I dont know I just did it and it ran.'''

start_time = time.time()
move_direction = DOWN
while True:
	delay = 1
	clock = pygame.time.Clock()
	clock.tick(80)/1000
	time_passed = round(time.time()-start_time,2)
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background, (0,0))
	if(coincount>5):
		coincount=0
	if(coincount1>15):
		coincount1=0
	if(coincount>2):
		coincount = 0
	
	#Draw board from the 2d layout array.
	#In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins

	'''getting the position of 
	the coins , walls and all. '''

	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos,coincount)
	coincount+=1
	coincount2=0
	#Draw the player
	draw_enemy(screen, enemy1_position, coincount2)
	coincount2+=1
	draw_enemy(screen, enemy2_position,coincount2)
	coincount2+=1
	draw_enemy(screen, enemy3_position,coincount2)
	coincount2+=1
	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down

	'''this part tells us about the key pressed 
	record it in a variable and then stores it
	to be used further''' 
	key = pygame.key.get_pressed()
	if key[K_UP]:
		move_direction = TOP
		state =0
	elif(key[K_DOWN]):
		move_direction = DOWN
		state =1
	elif(key[K_LEFT]):
		move_direction = LEFT
		state =2
	elif(key[K_RIGHT]):
		move_direction = RIGHT
		state =3

	draw_pacman(screen, pacman_position,coincount1,move_direction,state)
	coincount1+=1

	#tunnelcondition
	if(pacman_position[0]<=0 and move_direction==LEFT):
		pacman_position[0] = 19
	if(pacman_position[0]>=19 and move_direction == RIGHT):
		pacman_position[0] = 0

	'''checking for the walls and making it move accordingly'''

	if(move_direction==TOP):
		value = layout[int(pacman_position[1])][round(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==DOWN):
		value = layout[int(pacman_position[1]+1)][round(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==RIGHT):
		value = layout[round(pacman_position[1])][int(pacman_position[0])+1]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==LEFT):
		value = layout[round(pacman_position[1])][int(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	#Update player position based on movement.
	if move_direction == RIGHT or move_direction == LEFT:
		pacman_position = [pacman_position[0],round(pacman_position[1])]
	elif move_direction == TOP or move_direction==DOWN:
		pacman_position = [round(pacman_position[0]),pacman_position[1]]

	if(pacman_position[0]<=0 and move_direction==LEFT):
		pacman_position[0] = 19
	if(pacman_position[0]>=19 and move_direction == RIGHT):
		pacman_position[0] = 0

	if(move_direction==TOP):
		value = layout[int(pacman_position[1])][round(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==DOWN):
		value = layout[int(pacman_position[1]+1)][round(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==RIGHT):
		value = layout[round(pacman_position[1])][int(pacman_position[0])+1]
		if(value=='w'):
			move_direction = stop
	elif(move_direction==LEFT):
		value = layout[round(pacman_position[1])][int(pacman_position[0])]
		if(value=='w'):
			move_direction = stop
	#Update player position based on movement.
	if move_direction == RIGHT or move_direction == LEFT:
		pacman_position = [pacman_position[0],round(pacman_position[1])]
	elif move_direction == TOP or move_direction==DOWN:
		pacman_position = [round(pacman_position[0]),pacman_position[1]]

	#enemy
	'''this part does the same as pacman 
	part but for the three enemies and checks for 
	the same conditions vbut is taking direcctions randomly'''

	mog1=[]
	if(float(round(enemy1_position[0],2)).is_integer() and float(round(enemy1_position[1],2)).is_integer()):
		if(layout[round(enemy1_position[1])][round(enemy1_position[0])-1]!='w' and e1_direction!=RIGHT):
			mog1.append(LEFT)
		if(layout[round(enemy1_position[1])][round(enemy1_position[0])+1]!='w' and e1_direction!=LEFT):
			mog1.append(RIGHT)
		if(layout[round(enemy1_position[1])-1][round(enemy1_position[0])]!='w' and e1_direction!=DOWN):
			mog1.append(TOP)
		if(layout[round(enemy1_position[1])+1][round(enemy1_position[0])]!='w' and e1_direction!=TOP):
			mog1.append(DOWN)
		e1_direction = random.choice(mog1)

	'''just adding more comments'''

	if(enemy1_position[0]<=0 and e1_direction==LEFT):
		enemy1_position[0] = 19
	if(enemy1_position[0]>=18 and e1_direction == RIGHT):
		enemy1_position[0] = 0
	enemy1_position = add_to_pos(enemy1_position,e1_direction)

	'''part 2 to check it all that if there is a wall or not
	and how does it all work'''

	mog2=[]
	if(float(round(enemy2_position[0],2)).is_integer() and float(round(enemy2_position[1],2)).is_integer()):
		if(layout[round(enemy2_position[1])][round(enemy2_position[0])-1]!='w' and e2_direction!=RIGHT):
			mog2.append(LEFT)
		if(layout[round(enemy2_position[1])][round(enemy2_position[0])+1]!='w' and e2_direction!=LEFT):
			mog2.append(RIGHT)
		if(layout[round(enemy2_position[1])-1][round(enemy2_position[0])]!='w' and e2_direction!=DOWN):
			mog2.append(TOP)
		if(layout[round(enemy2_position[1])+1][round(enemy2_position[0])]!='w' and e2_direction!=TOP):
			mog2.append(DOWN)
		e2_direction = random.choice(mog2)
	
	#tunnel conditions

	if(enemy2_position[0]<=0 and e2_direction==LEFT):
		enemy2_position[0] = 19
	if(enemy2_position[0]>=18 and e2_direction == RIGHT):
		enemy2_position[0] = 0
	enemy2_position = add_to_pos(enemy2_position,e2_direction)

	mog3=[]
	'''sam thing for enemy 3'''

	if(float(round(enemy3_position[0],2)).is_integer() and float(round(enemy3_position[1],2)).is_integer()):
		if(layout[round(enemy3_position[1])][round(enemy3_position[0])-1]!='w' and e3_direction!=RIGHT):
			mog3.append(LEFT)
		if(layout[round(enemy3_position[1])][round(enemy3_position[0])+1]!='w' and e3_direction!=LEFT):
			mog3.append(RIGHT)
		if(layout[round(enemy3_position[1])-1][round(enemy3_position[0])]!='w' and e3_direction!=DOWN):
			mog3.append(TOP)
		if(layout[round(enemy3_position[1])+1][round(enemy3_position[0])]!='w' and e3_direction!=TOP):
			mog3.append(DOWN)
		e3_direction = random.choice(mog3)

	#tunnel conditions for the pacman and the enemy.
	
	if(enemy3_position[0]<=0 and e3_direction==LEFT):
		enemy3_position[0] = 19
	if(enemy3_position[0]>=18 and e3_direction == RIGHT):
		enemy3_position[0] = 0
	enemy3_position = add_to_pos(enemy3_position,e3_direction)

	'''if emeny caught the pacman we need to rest the game to inital position, so'''

	if((round(enemy1_position[0]),round(enemy1_position[1]))==(round(pacman_position[0]),round(pacman_position[1])) or (round(enemy2_position[0]),round(enemy2_position[1]))==(round(pacman_position[0]),round(pacman_position[1])) or (round(enemy3_position[0]),round(enemy3_position[1]))==(round(pacman_position[0]),round(pacman_position[1]))):
		lives-=1
		pacman_position = [1,1]
		enemy1_position = [8.0,6.0]
		enemy2_position = [9.0,6.0]
		enemy3_position = [10.0,6.0]
		time.sleep(1)
	#Update player position based on movement.	

	pacman_position = add_to_pos(pacman_position, move_direction)
	if(layout[round(pacman_position[1])][round(pacman_position[0])]=='c'):
		layout[round(pacman_position[1])][round(pacman_position[0])]='.'
		score+=10
		coinposx = random.randint(0,15)
		coinposy = random.randint(0,19)
		while (layout[coinposx][coinposy]=='w'):
			coinposx = random.randint(0,15)
			coinposy = random.randint(0,19)
		layout[coinposx][coinposy] = 'c'
		
	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array



	'''bliting gthe score and life's and time and every other thing'''
	'''world around is a pacman and thing assignment is trip and goes high
	as fully fleged scrap'''

	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render('Score = ' + str(score), False, (255, 0, 0))
	timesurface = myfont.render('Time = ' + str(time_passed), False, (255, 0, 255))
	screen.blit(textsurface,(0,0))
	screen.blit(timesurface,(128,0))
	#Update the display
	lpos =[(19,15),(18,15),(17,15)]
	for i in range(lives):
		draw_lives(screen,lpos[i])
	if(lives==0):
		time.sleep(1)
		#sleep time and displaying game over
		pygame.draw.rect(screen,(0,0,0),(50,100,550,250))
		myfont = pygame.font.SysFont('Comic Sans MS', 120)
		myfont1 = pygame.font.SysFont('Comic Sans MS', 80)
		#string and what not
		textsurface = myfont.render('GAME OVER', False, (0, 102, 204))
		timesurface = myfont1.render('Score = ' + str(score), False, (255, 25, 102))
		screen.blit(textsurface,(80,130))
		screen.blit(timesurface,(164,230))
		pygame.display.update()
		time.sleep(2)
		exit()
	#updating the screen
	pygame.display.update()
	#Wait for a while, computers are very fast.
	time.sleep(0.0001)