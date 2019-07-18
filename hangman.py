import random
#iter = 0


# A list of words that

potential_words = ["remarkable", "genius", "failure", "social", "complicated", "pixel", "yacht", "croquet"]



word = random.choice(potential_words)



# Use to test your code:

# print(word)

 #ME, shows the number of letters


# Converts the word to lowercase

word = word.lower()

length = len(word)
current_word =  ["_"] * length #ME it works!


# Make it a list of letters for someone to guess
 # TIP: the number of letters should match the word
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


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	#if guess in word:
		#for let in word:
			#current_word[iter]
		#iter += 1

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
