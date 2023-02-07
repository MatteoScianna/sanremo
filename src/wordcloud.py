#%%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import nltk
from nltk import word_tokenize
import nltk.data
nltk.download('vader_lexicon')
nltk.download('punkt')
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
#%%

def flatten(l):
    return [item for sublist in l for item in sublist]

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

l = word_count(unique_string)

# %%
directory = ""
dic_artist = {}
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f) as fu:
            contents = fu.read()
        dic_artist[f[:-4]] = {}
        dic_artist[f[:-4]]["full_text"] = contents
#%%
stop_words = set(stopwords.words('italian'))
stop_words1 = ["te","me","cosa","cose","d'","po","com","anch'",]

for key,value in dic_artist.items(): 
    new_string = re.sub(r'[^\w\s]', ' ', value["full_text"])
    new_string1 =new_string.lower()
    word_tokens = word_tokenize(new_string1)
    #they are present in stop_words or not
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    #with no lower case conversion
    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stop_words and w not in stop_words1:
            filtered_sentence.append(w)

    dic_artist[key]
    dic_artist[key]["filtered"] = filtered_sentence

#%%
list_full = []
for artista in dic_artist.keys():
    list_full.append(dic_artist[artista]["filtered"])
listona = flatten(list_full)
unique_string=(" ").join(listona)
dizionario = word_count(unique_string)
#%%
wordcloud = WordCloud(width = 1500, height = 1000,background_color="grey",colormap = "YlGnBu").generate_from_frequencies(dizionario)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()