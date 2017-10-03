from stop_words_and_clean import stop_clean
from nltk.tag import pos_tag_sents
from pprint import pprint
from collections import Counter
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
word_list = open("./news/reddit.txt", "r", encoding="utf-8").read()
liste=([i for i in word_list.lower().split() if i not in stop])

name_tag=[]
tag_tag=[]
for i,item in enumerate(liste):
    text = word_tokenize(liste[i])
    # print(text)
    zz=nltk.pos_tag(text)
    name_tag.append(zz[0][0])
    tag_tag.append(zz[0][1])

#Noun : NN
#Adjective : JJ
#Adverb : RB
#Verb : VBN
#VBG: Present Participle

print(Counter(name_tag))
print(Counter(tag_tag))
# nltk.help.upenn_tagset()
