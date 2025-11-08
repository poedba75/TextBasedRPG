# Import Full Libraries
import sys;

# Import Specific Modules from Libraries
from time import sleep;
from os import system, name;

# Import Python Scripts
import grid;

# Define Local variables.
zonemap = grid.zonemap;
find_princess = input("Do you want to find the princess? (yes/no): ").strip().lower();
match find_princess:
	case "yes":
		found_princess = False;
	case "no":
		found_princess = True;
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
		self.name = input("Enter your name: ");
		self.occupation = input("Enter your occupation: ");
		self.hp = 0;
		self.mp = 0;
		self.strength = 0;
		self.location = "0,0"; #Home Location
		self.gameover = False;

#does special things depending on what you do
match self.occupation:
	case "knight":
		self.hp = 100;
		self.mp = 50;
		self.strength = 100;
	case "mage":
		self.hp = 75;
		self.mp = 100;
		self.strength = 75;
	case "thief":
		self.hp = 60;
		self.mp = 75;
		self.strength = 60;		
	case "cleric":
		self.hp = 80;
		self.mp = 80;
		self.strength = 80;
	case "archer":
		self.hp = 90;
		self.mp = 60;
		self.strength = 85;
	case "bard":
		self.hp = 70;
		self.mp = 70;
		self.strength = 70;
	case "Barrel Worker":
		self.hp = 200;
		self.mp = 20;
		self.strength = 500;
		print("As a Barrel Worker, you have exceptional durability but limited magical ability.");
	case "Dragon Tamer":
		self.hp = 150;
		self.mp = 100;
		self.strength = 100;
	case "Alchemist":
		self.hp = 80;
		self.mp = 120;
		self.strength = 70;
	case "":
		print("No occupation selected. Defaulting to Adventurer.");
		self.hp = 85;
		self.mp = 85;
		self.strength = 85;	

# Initialize myPlayer
myPlayer = player();

# Define Local Dictionaries
valid_start_commands = ["play","help","quit","print map"];

###  Game Interactivity   ####
ZONENAME = "ZoneName";
DESCRIPTION = "Description";
EXAMINATION = "Examination";
ZONETYPE = "ZoneType";
UP = "North";
DOWN = "South";
LEFT = "West";
RIGHT = "East";

### Supporting Functions  ###
def printbychar(statement,ms=10):
	for character in statement:
		sys.stdout.write(character);
		sys.stdout.flush();
		sleep(ms * .001);

# Define Title Screen Selections
def title_screen_selections():
    printbychar("What would you like to do?");
    option = input("> ");
    
    while option.lower() not in valid_start_commands:
        printbychar("Please enter a valid command.");
        option = input("> ");

    if (option.lower() == "play"):
        start_game();
    elif (option.lower() == "help"):
        help_menu();
        title_screen_selections()
    elif (option.lower() == "print map"):
        printbychar("You can only print the map once you have started the game.\n");
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

def print_location():
	printbychar("\n" + zonemap[myPlayer.location][DESCRIPTION]);

def verify_action(action):
	acceptable_actions = ["move","go","travel","walk","examine","inspect","interact","look","help","quit","print map","show map"];
	new_action = action;

	while new_action.lower() not in acceptable_actions:
		printbychar("Unknown action, try again.\n");
		printbychar("Accepable actions include...\n");
		for acceptable_action in acceptable_actions:
			printbychar(acceptable_action + "\n");
		printbychar("\nWhat would you like to do?");
		new_action = input("\n" + myPlayer.location + "> ");
	return new_action;

def prompt():
	printbychar("\nWhat would you like to do?");
	action = input("\n" + myPlayer.location + "> ");
	verified_action = verify_action(action);

	match verified_action.lower():
		case "quit":
			sys.exit();
		case "help":
			help_menu();
		case "move"|"go"|"travel"|"walk":
			player_move(verified_action.lower());
		case "examine"|"inspect"|"interact"|"look":
			player_examine(verified_action.lower());
		case "print map"|"show map":
			grid.printmap(myPlayer.location);

def player_move(myAction):
	printbychar("\nWhere would you like to move to?");
	dest = input("\n" + myPlayer.location + "> ");

	match dest.lower():
		case "up"|"north":
			destination = zonemap[myPlayer.location][UP];
		case "down"|"south":
			destination = zonemap[myPlayer.location][DOWN];
		case "left"|"west":
			destination = zonemap[myPlayer.location][LEFT];
		case "right"|"east":
			destination = zonemap[myPlayer.location][RIGHT];
		case _:
			printbychar ("Invalid Direction");
			prompt();
		
	match destination:
		case "":
			move_stmt = "You can't move here.";
			printbychar(move_stmt);
		case "wall":
			move_stmt = "You can't continue.  There is a large wall here.";
			printbychar(move_stmt);
		case "thick forest":
			move_stmt = "The forest is too thick.  You can't go this way.";
			printbychar(move_stmt);
		case "cliff":
			move_stmt = "You stand in front of a huge cliff.  The rocks are too smooth to climb.";
			printbychar(move_stmt);
		case "cave wall":
			move_stmt = "You look around in the dark but there is no way out here.";
			printbychar(move_stmt);
		case _:
			movement_handler(destination);

def movement_handler(destination):
	printbychar("\n" + "You have moved to " + zonemap[destination][ZONENAME]+ ".");
	myPlayer.location = destination;
	print_location();

def player_examine(action):
	printbychar(zonemap[myPlayer.location][EXAMINATION]);

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
	printbychar("Hello, what is your name?\n");
	myPlayer.name = input("> ");

	### Introdution  ###
	printbychar("\nWelcome " + myPlayer.name + ".");
	printbychar("\nLet the Game Begin...");
	main_game_loop();

title_screen();