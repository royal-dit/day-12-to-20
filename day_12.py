#number guessing game my try
import random
print("Welcome to the number guessing Game")
print("i am thinking a number between 1 and 100")
diff_level = input("choose a  difficulty.Type 'hard' or 'easy'")

def random_func():
    rand_num = random.randint(1,100)
    return rand_num
def difficulty(diff_level,rand_out):
    if diff_level == 'hard':
        i = 5
        while i > 0:
            print(f"you have {i} attempts left guess the number")
            guess = int(input("make a guess:"))
            if guess > rand_out():
                print("Too high")
                print ("guess again")
            elif guess < rand_out:
                print("Too low")
                print("guess again")
            elif guess == rand_out:
                print("You guessed right number")
                break
            i -= 1
        return guess
    elif diff_level =='easy':
        i = 10
        while i > 0:
            print(f"you have {i} attempts left guess the number")
            guess1 = int(input("make a guess:"))

            if guess1 > rand_out:
                print("Too high")
                print("guess again")

            elif guess1 < rand_out:
                print("Too low")
                print("guess again")

            elif guess1 == rand_out:
                print("You guessed right number")
                break

            i -= 1

        return guess1



difficulty(diff_level,random_func())


