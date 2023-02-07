import pandas as pd
import os 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
#follow the instructions to install the packages https://nicgian.github.io/Sentita/
from sentita import calculate_polarity


#%%
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
for key,value in dic_artist.items():
    polarity = calculate_polarity([value["full_text"]])[1][0]
    dic_artist[key]["positive"] = polarity[0]
    dic_artist[key]["negative"] = polarity[1]
df = pd.DataFrame(dic_artist).transpose()

#%%
sns.lmplot( x="negative", y="positive", data=df, fit_reg=False, legend=False, height=20, aspect=1.3,scatter_kws={"s": 200})
for index in df.index:
    plt.annotate(index, (df["negative"][index], df["positive"][index]), (df["negative"][index]+0.0007, df["positive"][index]+0.0007), fontsize=20)
plt.suptitle('Song Map: Positive vs Negative sentiment score (lyrics)', fontsize=30)
plt.xlabel('Negative', fontsize=30)
plt.ylabel('Positive', fontsize=30)
plt.show()