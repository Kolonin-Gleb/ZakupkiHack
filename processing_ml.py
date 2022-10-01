# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 22:12:05 2022

@author: Vasily
"""

import pandas as pd
import numpy as np
import pickle
import heapq
from string import punctuation
from tqdm import tqdm
import nltk
nltk.download("stopwords")
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
russian_stop = stopwords.words('russian')

"""
Все файлы можно найти тут : https://drive.google.com/drive/folders/16fyjPa11u3phBI_q7QgK2ShKlltEh91r?usp=sharing
"""


def text_processing(text:str):
    tokens = [token for token in word_tokenize(text.lower()) if token not in russian_stop and token not in punctuation and token != 'none']
    text = " ".join(tokens)
    return text

processing_columns = ['product_name', 'product_msr', 'product_characteristics', 'okpd2_name', 'country_code']
df_groups = pd.read_csv('path/groups_dataframe', low_memory=False)
df_groups = df_groups.replace(np.nan, 'none')
for name in tqdm(processing_columns):
    df_groups[name] = df_groups[name].map(lambda x: text_processing(x))
    
df_ml = pd.DataFrame()
df_ml['product'] = (df_groups.product_name + ' '+df_groups.product_characteristics +' '+df_groups.okpd2_name + ' '+df_groups.product_msr + ' '+df_groups.country_code).replace('||', '')
df_ml['code'] = df_groups.okpd2_code


filename = 'path/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

text = 'сдвоенная шестерня'
prediction = loaded_model.predict([text])
prediction_proba = loaded_model.predict_proba([text])

code_probs = heapq.nlargest(10, prediction_proba[0])
find_codes = []
for code in code_probs:
    for i in range(len(prediction_proba[0])):
        if prediction_proba[0][i] == code: find_codes.append(loaded_model.classes_[i])

print(find_codes)