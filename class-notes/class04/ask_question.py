
name = input("what is your name?")

target = 50
guess = int(input("Guess what number I am thinking of? "))
print(f"Your guess is {guess}")
if guess == target:
    print("You are correct")
else:
    print("You are incorrect")
