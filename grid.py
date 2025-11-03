
# Import Supporting Modules
import random

# Import Specific Modules from Libraries
from time import sleep

# Get the dimensions of the playing grid
mapwidth = 70
mapheight = 13
princess_in_hiding = False

# If you want to prompt the user for the map size...
'''
mapwidth = int(input('What is the requested map width? (1-35)\n> '))
mapheight = int(input('What is the requested map height? (1-26)\n> '))
'''

# Define variables & Set Initial Values
map_area = mapwidth * mapheight
x = 0 #Horizontal Coordinates
y = 0 #Verticalll Coordinates
kings_possible_codes = ["Raven","Sheild","Sword","Dream","Dedication","Nobility"]
kings_code_index = random.randint(1,len(kings_possible_codes))-1
kings_code = kings_possible_codes[kings_code_index]

ZONENAME = "ZoneName"
DESCRIPTION = "Description"
EXAMINATION = "Examination"
ZONETYPE = "ZoneType"
UP = "Up","North"
DOWN = "Down","South"
LEFT = "Left","West"
RIGHT = "Right","East"
PRINCESS = False

# Initialize the Town_Zone Dictionary
Town_Zone = {}

# Populate the Town_Zone Dictionary
Town_Zone.update({
    '0,0' : {
        ZONENAME:"Your Home",
        DESCRIPTION:"Nothing appears to be out of place here.",
        EXAMINATION:"You find a note slipped under the door.  It reads 'I need your help.  Please meet me at the Town Square.'",
        ZONETYPE:"Town",
        UP:"",
        DOWN:"0,1",
        LEFT:"",
        RIGHT:"1,0",
        PRINCESS:False,
    }
})

Town_Zone.update({
    '0,1' : {
        ZONENAME:"The Town Square",
        DESCRIPTION:"Many of the town's people are here sharing news and talking.",
        EXAMINATION:"A hooded man approaches you and tells you his daughter has been kidnapped.  He needs you to rescue her.\nHe says you'll need to remember \"" + kings_code + "\" when you find his daughter.",
        ZONETYPE:"Town",
        UP:"0,0",
        DOWN:"",
        LEFT:"",
        RIGHT:"1,1",
        PRINCESS:False,
    }
})

Town_Zone.update({
    '1,0' : {
        ZONENAME:"The Tavern",
        DESCRIPTION:"You will never find a more wretched hive of scum and villainy. We must be cautious.",
        EXAMINATION:"This place is full of smugglers, thieves and swindlers.",
        ZONETYPE:"Town",
        UP:"",
        DOWN:"1,1",
        LEFT:"0,0",
        RIGHT:"",
        PRINCESS:False,
    }
})

Town_Zone.update({
    '1,1' : {
        ZONENAME:"The Town Entrance",
        DESCRIPTION:"This is the only way in or our of town.",
        EXAMINATION:"The town is protected by a tall stone wall with one monstrous iron gate.",
        ZONETYPE:"Town",
        UP:"1,0",
        DOWN:"1,2",
        LEFT:"0,1",
        RIGHT:"2,1",
        PRINCESS:False,
    }
})

random_princess_x = 0
random_princess_y = 0
princess_location = str(random_princess_x) + "," + str(random_princess_y)

while princess_location in Town_Zone:
    random_princess_y = random.randint(1,mapheight-1)
    random_princess_x = random.randint(1,mapwidth-1)
    princess_location = str(random_princess_x) + "," + str(random_princess_y)

# Initialize the ZoneMap Dictionary
zonemap = {}

while y < mapheight:
    while x < mapwidth:
        # Define Current and Neighbor Coordinates
        curr_coordinate = str(x) + "," + str(y)
        
        if y == 0:
            up_coordinate = ""
        else:
            up_coordinate = str(x) + "," + str(y-1)

        if (y+1) == mapheight:
            down_coordinate = ""
        else:   
            down_coordinate = str(x) + "," + str(y+1)

        if x == 0:
            left_coordinate = ""
        else:
            left_coordinate = str(x-1) + "," + str(y)

        if (x+1) == mapwidth:
            right_coordinate = ""
        else:   
           right_coordinate = str(x+1) + "," + str(y)

        if up_coordinate in Town_Zone and Town_Zone[up_coordinate][ZONENAME] != "The Town Entrance":
            up_coordinate = "wall"

        if down_coordinate in Town_Zone and Town_Zone[down_coordinate][ZONENAME] != "The Town Entrance":
            down_coordinate = "wall"

        if right_coordinate in Town_Zone and Town_Zone[right_coordinate][ZONENAME] != "The Town Entrance":
            right_coordinate = "wall"

        if left_coordinate in Town_Zone and Town_Zone[left_coordinate][ZONENAME] != "The Town Entrance":
            left_coordinate = "wall"

        # Populate the Map with 55% Open Field, 5% Caves and the rest as Forest
        random_int = random.randint(1,100)

        if random_int <= 55:
            zonetype_value = "Open Field"
            zonename_value = "an open field"
           
        elif random_int <= 60:
            zonetype_value = "Cave"
            zonename_value = "a cave"

            random_obstacle_int = random.randint(1,100)
            if random_obstacle_int <= 25:
                right_coordinate = "cave wall"
                down_coordinate = "cave wall"
                left_coordinate = "cave wall"
            elif random_obstacle_int <= 50:
                up_coordinate = "cave wall"
                down_coordinate = "cave wall"
                left_coordinate = "cave wall"
            elif random_obstacle_int <= 75:
                up_coordinate = "cave wall"
                right_coordinate = "cave wall"
                left_coordinate = "cave wall"
            else:
                up_coordinate = "cave wall"
                right_coordinate = "cave wall"
                down_coordinate = "cave wall"
        else:
            zonetype_value = "Forest"
            zonename_value = "the forest"

            random_obstacle_int = random.randint(1,100)
            if random_obstacle_int < 5:
                up_coordinate = "cliff"
            elif random_obstacle_int < 10:
                up_coordinate = "thick forest"

            random_obstacle_int = random.randint(1,100)
            if random_obstacle_int < 5:
                down_coordinate = "cliff"
            elif random_obstacle_int < 10:
                down_coordinate = "thick forest"

            random_obstacle_int = random.randint(1,100)
            if random_obstacle_int < 5:
                right_coordinate = "cliff"
            elif random_obstacle_int < 10:
                right_coordinate = "thick forest"

            random_obstacle_int = random.randint(1,100)
            if random_obstacle_int < 5:
                left_coordinate = "cliff"
            elif random_obstacle_int < 10:
                left_coordinate = "thick forest"

        description_value = "This will store the description of the zone."
        examination_value = "This will be the message upon examination of the current zone."
        
        if curr_coordinate in Town_Zone:
            zonename_value = Town_Zone[curr_coordinate][ZONENAME]
            description_value = Town_Zone[curr_coordinate][DESCRIPTION]
            examination_value = Town_Zone[curr_coordinate][EXAMINATION]
            zonetype_value = Town_Zone[curr_coordinate][ZONETYPE]
            up_coordinate = Town_Zone[curr_coordinate][UP]
            down_coordinate = Town_Zone[curr_coordinate][DOWN]
            left_coordinate = Town_Zone[curr_coordinate][LEFT]
            right_coordinate = Town_Zone[curr_coordinate][RIGHT]
            princess = Town_Zone[curr_coordinate][PRINCESS]
        elif curr_coordinate == princess_location and princess_in_hiding == False:
            princess = True
            princess_in_hiding = True
        else:
            princess = False

        # Add Entry to zonemap Dictionary        
        zonemap.update({ 
            curr_coordinate: {
                ZONENAME:zonename_value,
                DESCRIPTION:description_value,
                EXAMINATION:examination_value,        
                ZONETYPE:zonetype_value,
                UP:up_coordinate,
                DOWN:down_coordinate,
                LEFT:left_coordinate,
                RIGHT:right_coordinate,
                PRINCESS:princess,
            },
        })

        x += 1
    
    y += 1
    x = 0

def printmap (curr_location):
    y = 0
    x = 0

    print ("-" * (mapwidth+2))

    while y < mapheight:
        
        xline = "|"
        
        while x < mapwidth:
            curr_coordinate = str(x)+","+str(y)

            if curr_coordinate == curr_location:
                mapicon = "*"
            elif zonemap[curr_coordinate][ZONENAME] == "Your Home":
                mapicon = "H"
            elif zonemap[curr_coordinate][ZONETYPE] == "Town":
                mapicon = "T"
            elif zonemap[curr_coordinate][ZONETYPE] == "Forest":
                mapicon = "F"
            elif zonemap[curr_coordinate][ZONETYPE] == "Open Field":
                mapicon = " "
            elif zonemap[curr_coordinate][ZONETYPE] == "Cave":
                mapicon = "C"
            else:
                mapicon = "X"

            xline = xline + mapicon + ""

            x += 1
        xline = xline + "|"
        print(xline)
        sleep(.005)

        x = 0
        y += 1
    print ("-" * (mapwidth+2))

    print ("-----------Legend------------")
    print ("| * = Your Current Location |")
    print ("| H = Your Home             |")
    print ("| T = Town Area             |")
    print ("| F = Forest                |")
    print ("| <Blank> = Open Field      |")
    print ("| C = Cave                  |")
    print ("-----------------------------")