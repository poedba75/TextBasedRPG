# Import Full Libraries
import sys;

# Import Specific Modules from Libraries
from time import sleep;
from os import system, name;

# Import Python Scripts
import grid;

# Define Local variables.
zonemap = grid.zonemap;
found_princess = False;

# Python Test RPG
# Name here :D
# Must be run in Python3

# Clear the screen
if name == "nt":
	clear_command = "cls";
else:
	clear_command = "clear";

# Define Player Class with attributes
class player:
	def __init__(self):
		self.name = "";
		self.occupation = "";
		self.hp = 0;
		self.mp = 0;
		self.location = "0,0"; #Home Location
		self.gameover = False;

# Initialize myPlayer
myPlayer = player();

# Define Local Dictionaries
valid_start_commands = ["play","help","quit","print map"];

### Supporting Functions  ###
def printbychar(statement,ms):
	for character in statement:
		sys.stdout.write(character);
		sys.stdout.flush();
		sleep(ms * .001);

# Define Title Screen Selections
def title_screen_selections():
    printbychar("What would you like to do?",20);
    option = input("> ");
    
    while option.lower() not in valid_start_commands:
        printbychar("Please enter a valid command.",20);
        option = input("> ");

    if (option.lower() == "play"):
        start_game();
    elif (option.lower() == "help"):
        help_menu();
        title_screen_selections()
    elif (option.lower() == "print map"):
        printbychar("You can only print the map once you have started the game.\n",20);
        title_screen_selections();
    elif (option.lower() == "quit"):
        sys.exit();

def title_screen():
    system(clear_command);
    print("###########################");
    print("# Welcomd to the TextRPG! #");
    print("###########################");
    print("          - Play -         ");
    print("          - Help -         ");
    print("          - Quit -         ");
    print("   Copyright 2020 me.me    ");
    print("###########################");
    title_screen_selections();

def help_menu():
    print("Help Menu");
    print("- Type your commands to do them");
    print("- Use [look] to get more details of a location.");
    print("- Use [go] to move to a new location.");
    print("- Valid Directions are [north,east,south,west]");
    print("- Good Luck and have fun!");
    
###  Game Interactivity   ####
ZONENAME = "ZoneName";
DESCRIPTION = "Description";
EXAMINATION = "Examination";
ZONETYPE = "ZoneType";
UP = "North";
DOWN = "South";
LEFT = "West";
RIGHT = "East";

def print_location():
	printbychar("\n" + zonemap[myPlayer.location][DESCRIPTION],20);

def prompt():
	acceptable_actions = ["move","go","travel","walk","examine","inspect","interact","look","help","quit","print map","show map"];

	printbychar("\nWhat would you like to do?",20);
	action = input("\n" + myPlayer.location + "> ");

	while action.lower() not in acceptable_actions:
		printbychar("Unknown action, try again.\n",20);
		printbychar("Accepable actions include...\n",20);
		for acceptable_action in acceptable_actions:
			printbychar(acceptable_action + "\n",20);
		action = input("\n" + myPlayer.location + "> ");

	if action.lower() == "quit":
		sys.exit();
	elif action.lower() == "help":
		help_menu();
	elif action.lower() in ["move","go","travel","walk"]:
		player_move(action.lower());
	elif action.lower() in ["examine","inspect","interact","look"]:
		player_examine(action.lower());
	elif action.lower() in ["print map","show map"]:
		grid.printmap(myPlayer.location);

def player_move(myAction):
	printbychar("\nWhere would you like to move to?",20);
	dest = input("\n" + myPlayer.location + "> ");
	if dest.lower() in ["up","north"]:
		destination = zonemap[myPlayer.location][UP];
	elif dest.lower() in ["down","south"]:
		destination = zonemap[myPlayer.location][DOWN];
	elif dest.lower() in ["left","west"]:
		destination = zonemap[myPlayer.location][LEFT];
	elif dest.lower() in ["right","east"]:
		destination = zonemap[myPlayer.location][RIGHT];
		

	if destination == "":
		move_stmt = "You can't move here.";
		printbychar(move_stmt,20);
	elif destination == "wall":
		move_stmt = "You can't continue.  There is a large wall here.";
		printbychar(move_stmt,20);
	elif destination == "thick forest":
		move_stmt = "The forest is too thick.  You can't go this way.";
		printbychar(move_stmt,20);
	elif destination == "cliff":
		move_stmt = "You stand in front of a huge cliff.  The rocks are too smooth to climb.";
		printbychar(move_stmt,20);
	elif destination == "cave wall":
		move_stmt = "You look around in the dark but there is no way out here.";
		printbychar(move_stmt,20);
	else:
		movement_handler(destination);

def movement_handler(destination):
	printbychar("\n" + "You have moved to " + zonemap[destination][ZONENAME]+ ".",20);
	myPlayer.location = destination;
	print_location();

def player_examine(action):
	printbychar(zonemap[myPlayer.location][EXAMINATION],20);

###  Game Functionality   ####
def start_game():
    setup_game();

def main_game_loop():
	while myPlayer.gameover is False:
		prompt();
		# here handle if puzzles are solved

def setup_game():
	# Clear the screen.
	system(clear_command);

	### Name Collection  ###
	printbychar("Hello, what is your name?\n",20);
	myPlayer.name = input("> ");

	### Introdution  ###
	printbychar("\nWelcome " + myPlayer.name + ".",20);
	printbychar("\nLet the Game Begin...",20);
	main_game_loop();

title_screen();