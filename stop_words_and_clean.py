from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
from collections import Counter
## stopwords path : C:\Users\{{user_name}}\AppData\Roaming\nltk_data\corpora\stopwords
def stop_clean(fn):
    stop = set(stopwords.words('en'))
    word_list = open(fn, "r",encoding="utf-8")
    z=list(word_list)

    isaretleme_listesi=(list(punctuation))
    words = [w.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('%', ' ').replace(':', ' ').replace(';', ' ')   for w in z]

    zz=[]
    for line in words:
        for w in line.split():
            if w.lower() not in stop:
                zz.append(w)
        return (zz)