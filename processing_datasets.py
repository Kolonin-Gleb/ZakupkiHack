# Файл для преобразования датасетов к формату, по которому будет производиться поиск

import pandas as pd
import numpy as np
import re
# Для преобразования датасетов к виду для поиска
from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm.notebook import tqdm

'''
# Important Note:
Для повторения и финального деплоя на сервер нужно будет
Добавить в папку datasets папку data c полными версиями датасетов (3 .csv файла)
'''

######## Открытие полных версий датасетов


# df_contract = pd.read_csv('datasets/data/Контракты 44ФЗ.csv', sep=';')
# df_guide = pd.read_csv('datasets/data/Справочник пром производства.csv', sep=';')
df_offer = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', sep=';')

######## Преобразование датасетов к виду для поиска

nltk.download("stopwords")
nltk.download('punkt')

df_offer = df_offer.replace(np.nan, 'none')

russian_stop = stopwords.words('russian')

processing_columns = ['product_name', 'product_msr', 'product_characteristics', 'okpd2_name']
# TODO: Функция Маши может плохо работать, если product_characteristics обрабатывается,
# т.к. она использует имеющиеся разделители
def data_processing(df: pd.DataFrame, processing_columns: list):
    for name in tqdm(processing_columns):
        df[name] = df[name].map(lambda x: text_processing(x))

def text_processing(text:str):
    tokens = [token for token in word_tokenize(text.lower()) if (token not in russian_stop and token not in punctuation)]
    text = " ".join(tokens)
    return text

# Тест функции

print("------------- Датасет до обработки -------------")
print(df_offer.head())
print("\n\n\n")
print("------------- Датасет после обработки -------------")
data_processing(df_offer, processing_columns)
print(df_offer.head())
print("\n\n\n")
# df_offer.to_csv('processed Ценовые предложения поставщиков.csv')



# Как убедиться в роботоспособности функции преобразования датасетов от Васи?
# Нужно глянуть DF до использования функции и после.


