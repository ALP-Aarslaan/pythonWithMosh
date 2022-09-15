guess_number = 1
while guess_number <= 5:
    print(guess_number)
    guess_number = guess_number + 1
print("done")

guess_number = 1
while guess_number <= 5:
    print("*" * guess_number)
    guess_number = guess_number + 1
print("done")

hidden_number = 9
i = 0
while i < 3:
    guess = int(input("guess a number : "))
    i = i + 1
    if guess == 9:
        print("you won, you guessed ",guess)
        break
else:
    print("you lost")

"""
while loop can have an else statement without an if statement 
"""
print("enter command to play with the car :")
command = " "
started = False
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car starts ")
    elif command == "stop":
        if not started:
            print("car already stopped ")
        else:
            started = False
            print("car stops")
    elif command == "help":
        print('''
-> start :  to start the car
-> stop : to stop the car
-> quit : to quit the game 
        ''')
    elif command == "quit":
        break
    else:
        print("sorry i don't understand ")
