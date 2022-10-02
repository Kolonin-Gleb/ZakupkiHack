######## Преобразование датасетов к виду словарей для
# Словари категория: [характеристики]
# Это позволит реализовать поиск по категориям и характеристикам.
# Код от Марии

import re
import pandas as pd

test = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', on_bad_lines='skip', sep=';')
test['product_characteristics'].fillna('NaN', inplace=True)
test['country_code'].fillna('NaN', inplace=True)

# key - value dictionary (series)
series_name_product = test['product_name']
series_key_test = test['okpd2_name']
series_charc_test = test['product_characteristics']
series_country_test = test['country_code']

# впомогательный список
series__test = []
# список с характеритиками каждого из ОКПД2
series_whole_charc_test = []

# вырез ненужной инфы из характеристик
for i in series_charc_test:
    w = re.sub(r"\:.*?\|","|",i)
    if w.find(':') != -1:
        a = w.index(':')
        w = w[:a]
    if w != 'N/A':
        series__test.append(w)
    else:
        series__test.append('')
for i in series__test:
    q = re.split("\|.*?\|", i)
    series_whole_charc_test.append(q)

# создание словаря к каждому ОКПД2 - список характеристик
dictionary_test = dict(zip(series_key_test, series_whole_charc_test))

# создание списка словарей с названием, окпд и характеристиками
keys = ['name', 'okpd2_name', 'characteristics', 'country']
zipped = zip(series_name_product, series_key_test, series_whole_charc_test, series_country_test)
all_in = [dict(zip(keys, values)) for values in zipped]

for i in range(20):
	print(all_in[i])


