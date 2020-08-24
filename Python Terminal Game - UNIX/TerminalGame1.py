import random as r
import os
#import keyboard

# Dictionary showing the layout of every possible game

pages = {
	"b":"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	0:"O 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	1:"0 0 0 0 0 0 0 0 0 0\n0 O 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	2:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 O 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	3:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 O 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	4:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 O 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	5:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 O 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	6:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 O 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	7:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 O 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	8:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 O 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0",
	9:"0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 O\n0 0 0 0 0 0 0 0 0 0"
}

# General variables
doggerPage = r.randint(1,10) # Randomly chooses which page the circle is on
Row = r.randint(0,9) # Chooses what row Dogger is on
doggerRow = pages[Row] # Takes the dictionary's definition of the row and holds it to be used
npPage = '' # The input variable for what the person is doing
currentDisplayPage = 1 # What page the user is on currently
Message = '' # Displays a message from the game
osType = os.name # Finds what OS the person is using (posix or nt/BASH shell or Powershell)
copyrightName = "Made by Isaac - GreenSphinx#0717\n" # My copyright


def newPage():	
	# Variables
	global currentDisplayPage
	global npPage
	global Message

	clearScreen() # Clears the terminal every refresh
	print("\n\n\n") # New lines for prettiness
	print(copyrightName) # Says it was made by GreenSphinx#0717

	if currentDisplayPage == doggerPage:
		print(doggerRow)
	else:
		print(pages["b"])
	
	print(Message)
	npPage = input("Next page, Previous page, Found, or Exit (%s out of 10) n/p/f/e: " %(currentDisplayPage))
	npPage = npPage.lower()
	Message = ''
	newPageCheck()	

def newPageCheck():
	# Variables
	global currentDisplayPage
	global npPage
	global doggerPage
	global Message

	if npPage == 'n':
		if currentDisplayPage < 10:
			# Update Vars
			currentDisplayPage+=1
		else:
			currentDisplayPage = 1

		# Rerun
		newPage()
	elif npPage == 'p':
		if currentDisplayPage > 1:
			# Update vars
			currentDisplayPage-=1
		else:
			currentDisplayPage = 10

		# Rerun
		newPage()
	elif npPage == 'f':
		if currentDisplayPage == doggerPage:
			clearScreen()
			print("\n\n\n\n\n\nCongratulations!\nYou won!")
			newGame()
		else:
			Message = "You did not find it!"

			# Rerun
			newPage()
	elif npPage == '' or npPage == ' ':
		newPage()
	elif npPage == 'e':
		clearScreen()
		print("\n\n\n\n\n\nGoodbye! We hope to see you again soon!\n\n\n\n\n\n")
		exit
	else:
		exit # redoAsk()

def newGame():

	global currentDisplayPage
	global npPage
	global doggerPage
	global Message
	global doggerRow

	replay = input("Would you like to start another game? (y/n): ")
	replay = replay.lower()

	if replay == 'y':

		# Change variables
		doggerPage = r.randint(1,10) # Randomly chooses which page Dogger is on
		Row = r.randint(0,9) # Chooses what row Dogger is on
		doggerRow = pages[Row] # Takes the dictionary's definition of the row and holds it to be used
		npPage = ''
		currentDisplayPage = 1
		Message = ''
	
		newPage()
	else:
		print("Goodbye! We hope to see you again soon!")
		exit

# || Driver Program ||
def clearScreen():
	if osType == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	
newPage() # Run the game