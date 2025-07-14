import random as r

n = r.randint(0,100)        # Random number is chosen

print('''==== NUMBER
             GUESSING
               GAME ====

    Enter only positive numbers (0-100):
            ''')

ct = 0

while True:     # Game starts
    try:
        c = int(input("Guess and enter any number you think: "))

        if n < 0:
            print("Please print positive numbers only. YOU ARE RUINING THE GAME.\n")
        
        else:
            if n == c:
                print("There u go. YOU GOT IT!! Thank you.\n")      # Game ends after correct guess

                print('Tries : ', ct)       
                break

            elif n < c and abs(n - c) > 9:
                print("Guessed number is right to the exact number. Keep it up.\n")
                ct += 1

            elif n > c and abs(n - c) > 9:
                print("Guessed number is left to the exact number. Keep it up.\n")
                ct += 1

            elif abs(n - c) <= 9:
                print('U are very close. Keep Trying.\n')
                ct += 1
    
    except:
        print("Please print positive numbers only. YOU ARE RUINING THE GAME.\n")