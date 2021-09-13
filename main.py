import pygame #import pygame module for the job

class Main: #create class for our game
	def __init__(self):
		pygame.init() #initialize pygame assets 
		#create window and pass it to the self.screen variable
		self.screen = pygame.display.set_mode((900, 650))
		#create caption for the window and call the game Time Fuzz
		pygame.display.set_caption("Time Fuzz")
		#here we're going to be creating some variables of fonts with 
		#various uses, such as normal text, title etc
		self.font = pygame.font.SysFont('comicsansms', 52)
		self.title = pygame.font.SysFont('magneto', 52)
		self.font1 = pygame.font.SysFont('informalroman', 60)
		self.font2 = pygame.font.SysFont('comicsansms', 32)
		#you can see the font and size has already been preselected
		#you can change them and play around with them, before that we'll
		#need to implement them, and here's how we'll do it
		self.draw() #call draw function defined below

	#To reduce the effor of typing the screen.blit stuff everytime we need to 
	#insert the text to the window, we'll need to define functions and put it in them
	#to make thet code more efficient, simpler shorter and faster, plus some other benefits
	def Text(self, text, color, x, y):
		self.screen.blit(self.font.render(text, 1, color), (x, y))
	def Title(self, text, color, x, y):
		self.screen.blit(self.title.render(text, 1, color), (x, y))
	def Text1(self, text, color, x, y):
		self.screen.blit(self.font1.render(text, 1, color), (x, y))
	def Text2(self, text, color, x, y):
		self.screen.blit(self.font2.render(text, 1, color), (x, y))
	#The funtions above take text, color, x and y as parameters that can easily
	#be filled when necessary, each function corresponds to each predefined font
	#that we did in the init function.

	#now let's make a use of them by starting the creation of the game menu
	#we'll do this in a new function:
	def draw(self):
		#open our image file path and store it in a variable
		bg = pygame.image.load('imgs/menu.jpg')
		#load and play music
		pygame.mixer.music.load('sound/bensound-epic.mp3')
		pygame.mixer.music.play()
		#render image on the screen from the top left corners
		self.screen.blit(bg, (0, 0))
		#create and set the transparent rectangle
		menu = pygame.Surface((300, 300))
		menu.fill((0,0,0))
		menu.set_alpha(50)
		#note that we wrote this before the text cause we want it
		#to be at the back of the text so it is ran first
		self.screen.blit(menu, (10, 140))
		#then we apply the text in the window by calling the text functions
		#that we defined
		self.Title("Time Fuzz", (255, 255, 255), 330, 10)
		self.Text("Play", (255, 255, 255), 20, 150)
		self.Text("About", (255, 255, 255), 20, 250)
		self.Text("Quit", (255, 255, 255), 20, 350)
		#So we call this function in the init function so that it would
		#run as soon as our program starts.

	def match_coord(self, x, y, w, h):
		if self.pos[0]>x and self.pos[0]<x+w:
			if self.pos[1]>y and self.pos[1]<y+h:
				return True

	def run(self): #this is the looping function, it’s necessary to make our game loop
		while True:
			#define a variable for storing the value of where the mouse is
			#located in the game window
			self.pos = pygame.mouse.get_pos()
			#check the pygame events for when the quit button is clicked
			#that is the close button of the window.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
				    quit()#the quit function in python:terminates the running program
				if event.type == pygame.MOUSEMOTION:#check for mouse moving events
					if self.match_coord(10, 140, 300, 100):#get coordinates of the mouse
						#draw a white rectangle everytime the mouse is in the area
						pygame.draw.rect(self.screen, (255, 255, 255), (310, 140, 3, 100))
					else:
						#change the color of the rectangle when the mouse leaves the
						#coordinates, we'll repeat it for the other 3 buttons
						pygame.draw.rect(self.screen, (0, 0, 255), (310, 140, 3, 100))
					if self.match_coord(10, 240, 300, 100):
						pygame.draw.rect(self.screen, (255, 255, 255), (310, 240, 3, 100))
					else:
						pygame.draw.rect(self.screen, (0, 0, 255), (310, 240, 3, 100))
					if self.match_coord(10, 340, 300, 100):
						pygame.draw.rect(self.screen, (255, 255, 255), (310, 340, 3, 100))
					else:
						pygame.draw.rect(self.screen, (0, 0, 255), (310, 340, 3, 100))
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.match_coord(10, 140, 300, 100):
						pass
						#you can replace pass with the game function where it will
						#begin when the user clicks play
					if self.match_coord(10, 240, 300, 100):
						pass
						#pass can be replace with a page where you wrote about the game
					if self.match_coord(10, 340, 300, 100):
						quit()
						#this exits the game when quit button isclicked

			pygame.display.update()#this is needed toupdate what we've drawn on the screen

#running our program:
if __name__=="__main__":
	Main().run() #run the main function and run the loop.
