'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
tweets = []
for tweet in tweetData:
    text = tweet["text"]
    tweets.append(text)
for i in tweets:
    tb = TextBlob(i)
    polar_score = tb.polarity
    polarity.append(polar_score)
    subjectivity_score = tb.subjectivity
    subjectivity.append(subjectivity_score)

length = len(tweets) + 1
polarity_value = 0
subjectivity_value = 0
for i in polarity:
    polarity_value += i

for i in subjectivity:
    subjectivity_value += i

averagepol = polarity_value / length
print(averagepol)

averagesub = subjectivity_value / length
print(averagesub)

#Histogram
plt.hist(polarity, bins=[-1, -.75, -0.5, -.25, 0, .25, 0.5, .75, 1])
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Tweet Polarity")
plt.axis([-1, 1, 0, 65])
plt.grid(True)
plt.show()


plt.hist(subjectivity, bins=[0, .25, .5, .75, 1])
plt.xlabel("Subjectivity")
plt.ylabel("Number of Tweets")
plt.title("Tweet Subjectivity")
plt.axis([0, 1, 0, 45])
plt.grid(True)
plt.show()

plt.scatter(polarity, subjectivity)
plt.title("Scatter Plot")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.show()

badwords = ["I", "am", "is", "are", "they", "will", "be", "because", "the", "The", "or", "of", "and", "you", "she", "can", "https",
"see", "with", "he", "to", "it", "should", "that", "would", "from", "your", "for", "our", "how", "could"]
alltweets = " "
alltweets = alltweets.join(tweets)
allwords = TextBlob(alltweets)
filteredwords = {}

wordList = allwords.words
for word in wordList:
    if word in badwords:
        continue
    elif len(word) < 3:
        continue
    elif word.isalpha() == False:
        continue
    else:
        filteredwords[word] = allwords.word_counts[word]

wordcloud = WordCloud().generate_from_frequencies(filteredwords)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()




# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)
