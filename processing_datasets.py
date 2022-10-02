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

######## Обработка полных версий датасетов


df_contract = pd.read_csv('datasets/data/Контракты 44ФЗ.csv', sep=';')
# df_guide = pd.read_csv('datasets/data/Справочник пром производства.csv', sep=';')
# df_offer = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', sep=';')

# Словарь iso-code: Country_name
df_country_old = pd.read_csv('datasets/country_directory.csv', sep=';')
country_dict = {}
for i in range(len(df_country_old)):
    country_dict[df_country_old.country_iso_code[i]] = df_country_old.country_name[i]

# Функция работает только для датасета Контракты 44ФЗ.csv
def replace_cod(x, country_dict):
    new_list = list(map(float, str(x).replace('|', ',').split(',')))
    return ' '.join([str(country_dict.get(item,item)) for item in new_list])

# Замена iso-номеров на страны
df_contract.country_code = df_contract.country_code.apply(lambda x: replace_cod(x, country_dict))
# df_guide.country_code = df_guide.country_code.map(country_dict)
# df_offer.country_code = df_offer.country_code.map(country_dict)

######## Преобразование датасетов к виду для поиска

nltk.download('stopwords')
nltk.download('punkt')

# df_offer = df_offer.replace(np.nan, 'none')
# df_guide = df_guide.replace(np.nan, 'none')
df_contract = df_contract.replace(np.nan, 'none')

russian_stop = stopwords.words('russian')

processing_columns = ['product_name', 'product_msr', 'product_characteristics', 'okpd2_name']
#TODO: Функция Маши может плохо работать, если product_characteristics обрабатывается,
# т.к. она использует имеющиеся разделители
def data_processing(df: pd.DataFrame, processing_columns: list):
    for name in tqdm(processing_columns):
        df[name] = df[name].map(lambda x: text_processing(x))

def text_processing(text:str, punctuation=punctuation, include_punctuation=True):
    if not include_punctuation: punctuation = ''
    tokens = [token for token in word_tokenize(text.lower()) if (token not in russian_stop and token not in punctuation and token != 'none')]
    text = " ".join(tokens)
    return text

# Тест функции

print("------------- Датасет до обработки -------------")
print(df_contract.head())
print("\n\n\n")
print("------------- Датасет после обработки -------------")
data_processing(df_contract, processing_columns)
print(df_contract.head())
print("\n\n\n")
# df_offer.to_csv('processed Ценовые предложения поставщиков.csv', index=False, sep=';')
# df_guide.to_csv('processed пром производства.csv', index=False, sep=';')
df_contract.to_csv('processed 44ФЗ.csv', index=False, sep=';')

# Обработка всех датасетов с сохранением



