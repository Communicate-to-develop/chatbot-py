import random

#functions are defined here
def hello_reply():
    #pls add some good english replies
    hello_replies = ["Hello!","Hi!","Hey there.","What's up?"]
    print(random.choice(hello_replies))

def roll_dice():
    print("You got",random.randint(1,6))

def toss_coin():
    print("You got",random.choice(["Heads","Tails"]))

def hand_cric():
    choice = input("Rock(1)/Paper(2)/Scissors(3) : ").lower()
    bot_choice = random.choice(["Rock","Paper","Scissors"])
    if choice == "rock" or choice == "1":
        if bot_choice == "Rock":
            print("I too chose Rock. It's a draw")
        elif bot_choice == "Paper":
            print("I chose Paper. You lost!")
        else:
            print("I chose Scissors. You won!")
    elif choice == "paper" or choice == "2":
        if bot_choice == "Rock":
            print("I chose Rock. You won!")
        elif bot_choice == "Paper":
            print("I too chose Paper. It's a draw!")
        else:
            print("I chose Scissors. You lost!")
    elif choice == "scissors" or choice == 3:
        if bot_choice == "Rock":
            print("I chose Rock. You lost!")
        elif bot_choice == "Paper":
            print("I chose Paper. You won!")
        else:
            print("I too chose Scissors. It's a draw!")
    else:
        print("That's not a valid option!")

#actual program starts here
while True:
    query = input("Command : ").lower()
    if query != "exit":
        if query == "hi" or query == "hello":
            hello_reply()
        elif query == "roll a dice":
            roll_dice()
        elif query == "toss a coin":
            toss_coin()
        elif query == "hand cricket":
            hand_cric()
        else:
            print("Sorry, couldn't understand that.")
    elif query == "exit":
        print("Closing program.")
        break