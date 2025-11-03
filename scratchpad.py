quit
import random

kings_possible_codes = ["Raven","Sheild","Sword","Dream","Dedication","Nobility"]
kings_code_index = random.randint(1,len(kings_possible_codes))-1
kings_code = kings_possible_codes[kings_code_index]
print (kings_code)
