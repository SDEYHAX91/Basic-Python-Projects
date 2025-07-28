import random as r

def guess(start, end):          ## FUNCTION

    while True:                 ## LOOP
        guess = r.randint(start, end)
        try:
            feedback = input(f'Is {guess} too high, or too low, or correct?   :').lower()
            if feedback == 'h':
                end = guess - 1     ## MODIFYING GUESS RANGE

            elif feedback == 'l':
                start = guess + 1

            elif feedback == 'c':
                print(f"\n🎉Hooray! I guessed your number {guess} correctly.\n") 
                print("Closing the game. Have a good day.\n")   
                break      

            else:
                print("I didn't get you buddy. :-C")

        except Exception as e:
            print("I guess that's not a good input.\n")

if __name__ == '__main__':      ## MAIN
    print("Lets play a game, where I will guess your number.")
    print("You tell me whether my guess is correct or not.\n")
    print("--------------------------------------------------")
    print('------================LETS START==============------\n')
    guess(1,100)
