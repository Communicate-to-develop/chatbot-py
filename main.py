import random

user_greetings = ["hi","hello","hey","hai","what's up","whats up","hey there"]
#functions are defined here
def hello_reply():
    #pls add some good english replies
    hello_replies = ["Hello!","Hi!","Hey there.","What's up?"]
    print(random.choice(hello_replies))

def rand_num(x):
    print(random.randint(1,x))

def toss_coin():
    print("You got",random.choice(["Heads","Tails"]))

def rps():
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

def pass_gen(x):
    pass_symbols = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','$','#','$','*','_','-','~']
    password = ""
    for i in range(0,x):
        password += random.choice(pass_symbols)
    print(password)

#actual program starts here
while True:
    query = input("Command : ").lower()
    if query != "exit":
        if query in user_greetings:
            hello_reply()
        elif query == "random number":
            dice_num = int(input("Number limit : "))
            rand_num(dice_num)
        elif query == "toss a coin":
            toss_coin()
        elif query == "rps":
            rps()
        elif query == "generate password":
            x = int(input("Enter length of password : "))
            pass_gen(x)
        else:
            print("Sorry, couldn't understand that.")
    elif query == "exit":
        print("Closing program.")
        break