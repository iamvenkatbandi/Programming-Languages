number = 63

while True:
    guess = int(input("Guess the Number: "))
    if guess > number:
        print("Your Guess",guess," is Too High")
        print("Try Again!")
    elif guess < number:
        print("Your Guess",guess,"is Too Low")
        print("Try Again!")
    else:
        print("Your Guess",guess,"is Correct")
        break
