

# --- Define your functions below! ---
def intro():
    print("Hello! Welcome to my chatbot!")
    name = input("What is your name?")
    process_name(name)

def process_input(answer):
    if answer == "green":
        print("No way, that's is my favorite too!")
    else:
        print("Awesome! My favorite color is green!")

def say_greeting():
    print("How are you doing?")

def say_default():
    print("Very cool!")

def process_name(name):
    print("Nice to meet you " + name)


def riddle_game(yes_no):
    answergame = ["yes", "Yes", "yeah", "sure", "yea"]
    if yes_no in answergame:
        response = input("You give someone a dollar. You are this person's brother, but the person is not your brother. How can that be?")
        newresponse = ["sister", "Sister", "It's my sister", "its my sisier", "it is my sister", "It is my sister"]
        if response in newresponse:
            print("Nice, you are very clever!")
        else:
            print("Nice try! The correct answer is that the person is your sister...")
    else:
        print("Okay!")

def hangman(shesays):
    answerhangman = ["yes", "Yes", "yeah", "sure", "yea"]
    if shesays in answerhangman:
        import random

        potential_words = ["remarkable", "genius", "failure", "social", "complicated", "pixel", "yacht", "croquet"]

        word = random.choice(potential_words)

        word = word.lower()

        length = len(word)
        current_word =  ["_"] * length #ME it works!

        guesses = []

        maxfails = len(word) + 2

        fails = 0


        while fails < maxfails:
        	guess = input("Guess a letter or word!")
        	#while guess not in guesses:
        	#guesses.append(guess)
        	if guess == word:
        		print("You win!")
        		break
        	elif guess in word:
        		print("Guessed correctly!")
        		for let in range(len(word)):
        			if word[let] == guess:
        				print(word[let])
        				current_word[let] = guess
        	else:
        		print("Guessed wrong!")
        		fails = fails+1
        		print("You have " + str(maxfails - fails) + " tries left!")

        	print(current_word)

        	if not "_" in current_word:
        		print("You won!")
        		break
    else:
            print("Okay! Maybe another time!")


# --- Put your main program below! ---

def main():
  intro()
  while True:
      answer = input("What is your favorite color? ")
      process_input(answer)
      yes_no = input("Do you want to play a game?")
      riddle_game(yes_no)
      shesays = input("Would you like to play a round of hangman?")
      hangman(shesays)
      print("Thank you for a great time! I had sooo much fun!!!")
      break



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
  main()
