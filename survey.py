#empty dictionary
import json

#survey questions
questions = ['What is your name?',
    'How old are you?',
    'What grade are you in?',
    'What is your favorite food?',
    'Where is your favorite place to go on vacation?']

#list of related keys
keys = ['name', 'age', 'grade', 'food', 'vacation']
all_users = []
 #loop through your list of survey questions and take use input for responses
done = 'yes'
while done == 'yes':
    survey = {}
    index = 0
    for i in questions:
        responses = input(i)
        survey[keys[index]] = responses
        index += 1
    all_users.append(survey)
    done = input('Would you like to go on? yes or no.')
with open('survey.json') as file:
    try:
        olddata = json.load(file)
    except ValueError:
        olddata = []
all_users.extend(olddata)
file.close()

f = open('survey.json', 'w')
json.dump(all_users, f)
file.close()
# print dictionary
print(all_users)

age16 = 0
age17 = 0
age = 0
for u in all_users:
    age += 1
    answ = u["age"]
    if answ == 16:
        age16 += 1
    else:
        age17 += 1
if age16 > age17:
    print(str(age16) + ' out of ' + str(age17) + ' are 16 years old!')
else:
    print(str(age17) + ' out of '  +str(age16) + ' are 17 years old')
