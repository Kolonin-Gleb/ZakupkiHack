"""
Должен вызываться с Фронтенда

Функция поиска должна принимать параметры с фото для того, чтобы её можно было дёрнуть.
Параметрами для ввода:

1 текстовый запрос
2 Страна(необязательно) - название или id?
3 Категория (необязательно)
4 Характеристики

Характеристики в формате {характеристика1:значение1, характеристика2 :значение2}
"""

import pandas as pd
import numpy as np
import re

######## Открытие полных версий датасетов


# df_contract = pd.read_csv('datasets/data/Контракты 44ФЗ.csv', sep=';')
# df_guide = pd.read_csv('datasets/data/Справочник пром производства.csv', sep=';')
df_offer = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', sep=';')

df_offer = df_offer.replace(np.nan, 'none')      # заменяем все значени Nan на строки

df_dict = df_offer.drop(['price', 'inn', 'okpd2_code','country_code'], axis=1).to_dict('records')  # отбросим ненужные для поиска столбцы и запишеи DataFrame в словарь
# print(df_dict[:10])

# Поиск исключая числовые значения
def find(df, df_dict, string:str):
    out = {}
    priority = {}   # чем выше приоритет, тем больше совпадений по запросу (для одного товара)
    words = [word for word in string.split(' ') if word.strip()]   # разделяем запрос на слова убрав лишние пробелы
    for word in words:   # проходимся по каждому слову из запроса
        first = True
        for i in range(len(df_dict)):   # проходимся по каждой строке из DataFrame
            r = re.compile(f"\w* {word} \w*")  # ищем по патерну 'что-то пробел нужное слово что-то'
            match = list(filter(r.findall, list(df_dict[i].values())))
            if match:   # eсли нашлось совпадение :
                if i not in out:   # Если продукт еще не был добавлен
                    out[i] = df.iloc[i]   # создаем поле с этим продуктом
                    priority[i] = 0   # даем ему низший приоритет
                elif first:
                    priority[i] += 1   # Если продукт уже добавлен - повышаем приоритет
    for k, p in priority.items():
        if p < max(priority.values()): out.pop(k)   # Оставляем товары с лучшим совпадением
    return(out)


# response = find(df_offer, df_dict, 'Лук')
# print(len(response))

# Для лемматизации
from pymystem3 import Mystem

# Необходимо исключать союзы и вводные слова
from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm.notebook import tqdm

nltk.download('stopwords')
nltk.download('punkt')

russian_stop = stopwords.words('russian')

def text_processing(text: str):
    tokens = [token for token in word_tokenize(text.lower()) if (token not in russian_stop and token not in punctuation)]
    text = " ".join(tokens)
    return text


text = "Стол для рисования"
text_2 = text_processing(text) # Запрос без союзов и предлогов
print(text_2)

m = Mystem()
lemmas = m.lemmatize(text_2)
lemmatised_search = ''.join(lemmas)
print(lemmatised_search)


response2 = find(df_offer, df_dict, lemmatised_search)
print(response2)

######## Поиск
# Вынесен в файл find.py



######## Сортировка результата поиска
#TODO: Принимает на вход DF от функции find
'''
Сортировка результата поиска по приоритету для пользователя
'''

######## Отображение отсортированного результата у Коли
'''
Код
'''

######## Подсчёт полезных статистик для пользователя
'''
Код
'''
