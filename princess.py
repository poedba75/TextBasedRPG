import random;

def set_princess_location (mapwidth,mapheight):
    # Move Princess outside of town.
    random_princess_y = random.randint(1,mapheight-1)                           # Choose random y coordinate
    random_princess_x = random.randint(1,mapwidth-1)                            # Choose randle x coordinate
    # Override Random Location for Testing
    random_princess_x = 2;
    random_princess_y = 2;
    princess_location = str(random_princess_x) + "," + str(random_princess_y)   # Update Princess Location in x, y format
    return princess_location;
