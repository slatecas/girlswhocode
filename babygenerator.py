#imports the ability to get a random number (we will learn more about this later!)

from random import *



#Create the list of words you want to choose from.

firstnames = ["Sally", "Nick", "Kirsten", "Lily", "Miguel", "Juliet", "Kim", "Brad", "Jimmy", "Natalie"]
lastnames = ["Smith", "Rock", "Gomez", "Walker", "Dern", "Romeo", "Bello", "Pitt", "Reynolds", "Slate"]


#Generates a random integer.

randomfirst = randint(0, len(firstnames)-1)
randomlast = randint(0, len(lastnames)-1)

print(firstnames[randomfirst] +" "+ lastnames[randomlast])
