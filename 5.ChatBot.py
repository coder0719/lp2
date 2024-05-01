import random

def greet():
    greetings = ["Hi there!", "Hello!", "Hey!"]
    print(random.choice(greetings))

def farewell():
    farewells = ["Goodbye!", "See you later!", "Bye!"]
    print(random.choice(farewells))

def age_guesser():
    print("I'm going to guess your age!")
    name = input("Firstly, what's your name? ")
    print(f"Nice to meet you, {name}!")

    year = int(input("What year were you born? "))
    age_guess = 2024 - year
    # Random initial guess

    # if gender.lower() == "male":
    #     age_guess += 5
    # elif gender.lower() == "female":
    #     age_guess

    print(f"I'm guessing you're around {age_guess} years old based on your birth year.")

def numgame():
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = int(input("You have to guess the number i have in my mind\nEnter your guess between 0-9 : "))
    b = random.choice(number)

    print("Alright Your Guessed Number was :" , a)


    if (a == b):
        print("OMG,,,,Perfect guess")

    while (a != b):
        if (a < b):
            print("Oops....Guess a little bit higher : ")
            a = int(input())
        if (a > b):
            print("Hehehe....Guess a little bit lower : ")
            a = int(input())
        if (a == b):
            print("Yoooooooo...Finally guessed it")

def chat():
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            greet()
        elif "bye" in user_input or "goodbye" in user_input:
            farewell()
            break
        elif "guess" in user_input:
            print("What do you want 'Me to guess your age' OR 'Wanna play number guessing game?' tell me")
        elif "age_guess" in user_input or "age" in user_input:
                age_guesser()
        elif "number" in user_input or "no." in user_input or "game" in user_input:
                numgame()


        #  elif "age" in user_input or "guess" in user_input or "how old" in user_input or "number" in user_input:
        #     age_guesser()

        elif "no" in user_input or "nope" in user_input or "wrong" in user_input or "incorrect" in user_input:
            age_guesser()
        else:
            responses = ["I'm not sure I understand.", "Could you please repeat that?", "Tell me more!"]
            print(random.choice(responses))

if __name__ == "__main__":
    print("Welcome to the Simple Chatbot!")
    print("Feel free to say hello, ask me to guess your age, or just chat with me.")
    chat()


#Install this in CMD
#pip install chatterbot

#in terminal
#pip install chatterbot
#or
#pip3 install chatterbot

#then

#sudo pip install chatterbot
#or
#sudo pip3 install chatterbot
