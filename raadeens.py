from random import randint

guess_round = 1 # Round of the question
user_guesses = 0 # Amount of guessed the user has given
score = 0 # Total score of the user

user_stopped = False # If the user has stopped the questions

while guess_round <= 20 and not user_stopped:

    answer = randint(1, 1000) # Random number between 1 and 1000

    guessed_right = False # If the user guessed it correcly


    # Ask the question 10 times if the user has not guessed it correctly
    while user_guesses < 10 and not user_stopped and not guessed_right:
        
        guess = input('Raad het getal (vul "stop" in als u wilt stoppen met raden): ').lower()

        # Check if it is a number
        try:
            if guess != "stop":
                guess = int(guess) 

        # If the user did not answered a number
        except ValueError:
            print("Vul een geldig getal in") 

        # If the user did choose a number
        else:   
            # If the user wants to stop
            if guess == "stop":
                user_stopped = True

            # If the user guessed it correctly
            if guess == answer: 
                print("Geraden")

                guessed_right = True # Go to the next question
                score += 1 # Add 1 point to the score

            # If the user did not guess it correctly
            else:  
                # if the user guess was 25 of the answer
                if abs (guess - answer) <= 25:
                    print("Je bent heel warm")
                
                # if the user guess was 50 of the answer
                elif abs(guess - answer) <= 50:
                    print("Je bent warm")
                
                # Check if the user guessed lower, or higher than the answer
                else:
                    higher_lower = "hoger" if guess < answer else "lager"
                    print(higher_lower)


            user_guesses += 1 # Total guessed of the user

    # If the question is over
    else:
        user_guesses = 0 # Reset the guesses of the user

        string = 'Uw score is: "' + str(score) + '"'
        print(string)

        next_number = input("Nog een getal raden (ja/nee): ").lower()

        # If the user wants to go to the next round
        if next_number == "ja":
            guess_round += 1
        
        # If the user wants to stop
        else:
            user_stopped = True # Go out of the questions