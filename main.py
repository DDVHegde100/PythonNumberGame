import random
    print("Guessing Game!")
        number=random.randint(1,9)
        chances=0
    print("Guess a number between 1 and 9!")
    
    while chances <5:
        guess=int(input("Enter a number"))
        
        if guess==number:
            print("Correct!")
            break
        
        elif guess < number:
            print("Oh no. Your guess is too low!")
            print("Guess a higher number.")
        else:
            print("Oh no. Your guess is too high!")
            print("Guess a lower number.")
            
            chances+=1
            if chances==5 and guess!= number:
                print("You ran out of guesses. Try again!")