# Python program to generate WordCloud

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv("USATODAY_tweets_clean.csv")


comment_words = ' '
stopwords = set(STOPWORDS)

#iterate through the csv file
for val in df.text:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    for words in tokens:
        comment_words = comment_words + words + ' '

    print(comment_words)
# for word in df.text:
#     print(word)

wordcloud = WordCloud(width = 800, height = 800,
                #max_words = 200,
                #max_font_size = 40,
                min_font_size = 10,
                random_state = 42,
                background_color ='black',
                stopwords = stopwords).generate(comment_words)#.generate(df['text'])
print(wordcloud.words_)
# plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
