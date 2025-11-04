# Import Supporting Modules
import random;

kings_possible_codes = ["Raven","Sheild","Sword","Dream","Dedication","Nobility"]   # All Possible King Secret Codes
kings_code_index = random.randint(1,len(kings_possible_codes))-1                    # Randomly pick the index for one of the possible king secret codes
kings_code = kings_possible_codes[kings_code_index]                                 # Assign the King's Secret Code
