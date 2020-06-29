#coding a darn game
#shoot the fruit
#check the readme to get full brief
from random import randint #making the game the way enjoyable using random stuffs
orange = Actor("orange")
def draw(): #drawing our orange or whatever
	screen.clear()
	orange.draw()

def place_orange(): #you can change it according to your windows size. I put it
#approximate for your usage.
	orange.x = randint(10, 500) #you don't know what the position of the x axis will be.
	orange.y = randint(10, 500)	#same for y-axis




def on_mouse_down(pos):
#basically, pos is some kinda things to deal with "matching". That means
#if your cursor matches with your fruit, then you gotcha.
	if orange.collidepoint(pos):
#collides with the position and the cursor
		print("Hey, how you been so good at it?")
		place_orange() #recalling the function above
		

	else:
		print("Gotcha. Go, try some kinda bubble shuter. *should print spelling error xD*")
		quit()

place_orange()