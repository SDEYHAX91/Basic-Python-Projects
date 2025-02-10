import string
import random # IMPORTING STRING AND RANDOM LIBRARY

def Password_Generator(): # ONLY 15 CHARACTERS
    
    passw = [random.choice(string.ascii_uppercase), #PASSWORD AS LIST
             random.choice(string.ascii_lowercase),
             random.choice(string.digits),
             random.choice(string.punctuation)] #INITIALLY THERE MUST BE AT LEAST 1 UPPER CASE,
                                                # 1 LOWER CASE, 1 NUMBER AND 1 SPECIAL SYMBOL
    
    poss = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    passw += [random.choice(poss) for i in range(11)] #ADDING RANDOM CHARACTERS
    
    random.shuffle(passw) #SHUFFLING 
    password = ''.join(passw) #NOW STRING
    return password #O/P
