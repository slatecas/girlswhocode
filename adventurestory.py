start =  '''
Oh no! I need your help!
The diamond my grandmother gave me is missing!
But here is a note...
It says I have your diamond.
It is hidden on top of Mount Pebble.
I guess I should start searching for it...
Which way should I go to get to Mount Pebble ASAP?
Through the city or the desert?
''' # Update to match your story.
print (start)
user_input = input("Type 'city' to go to the city or 'desert' to go to the desert.")
if user_input == "city":
    print ("I have arrived at the city. Should I go through the wetlands or the woods")
    user_input = input("Type 'wetlands' to go to the wetlands or 'woods' to go to the woods.")
    if user_input == "wetlands":
        print ("Ouch a snake bit me! I need to go to the hospital. Looks like my diamond will never be found!")
    if user_input == "woods":
        print ("Look there in the distance is Mount Pebble! Let's go!")
        print ("Congratulations, we have reached the mountain! There is my diamond, thank you for your help!")
else:
    print ("Now should I go left or right.")
    user_input = input("Type 'left' to go to the left or 'right' to go to the right.")
    if user_input == "left":
        print ("I have arrived in the Savannah Desert. Should I take a dangerous short cut to the mountain or play it safe and go the long way?")
        user_input = input("Type 'short cut' or 'long way' to get to the mountain.")
        if user_input == "short cut":
            print ("Ouch, a lion mauled me! I'll never find my diamond now!")
        if user_input == "long way":
            print ("I see the mountain off in the distance! Let's go!")
            print ("Congratulations, you have arrived at the mountain!")
            print ("There is my diamond! Thank you!")
    if user_input == "right":
        print ("I have arrived at the park.")
        print ("I see the mountain off in the distance! Let's go!")
        print ("Congratulations, you have arrived at the mountain!")
        print ("There is my diamond! Thank you!")
