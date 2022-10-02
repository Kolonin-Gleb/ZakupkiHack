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

# Для поиска
import pandas as pd
import numpy as np
import re

# Для лемматизации поискового запроса
from pymystem3 import Mystem

# Для исключения союзов и вводных слов
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


def preparing_search_query(original_search_query: str):
    # Подготовка запроса для осуществления поиска
    # original_search_query = "Стол для рисования"
    cleaned_search_query = text_processing(original_search_query) # Запрос без союзов и предлогов
    print(cleaned_search_query)

    m = Mystem()
    lemmas = m.lemmatize(cleaned_search_query) # Запрос в стандартном виде
    lemmatised_search = ''.join(lemmas)
    print(lemmatised_search)
    return lemmatised_search

'''
Если передают категорию, то искать внутри категории + по параметрам
'''

######## Открытие датасета Ценновых предложений для осуществления поиска
df_offer = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', sep=';')
df_offer = df_offer.replace(np.nan, 'none') # заменяем все значени Nan на строки
df_dict = df_offer.drop(['price', 'inn', 'okpd2_code','country_code'], axis=1).to_dict('records')  # отбросим ненужные для поиска столбцы и запишеи DataFrame в словарь

def search(query: str, country_name = "", category = "", params = []):
    lemmatised_search = preparing_search_query(query)
    response2 = find(df_offer, df_dict, lemmatised_search) # Поиск идёт только в df_offer
    print(response2)
    print(type(response2))
    return response2


# Поиск только среди ценновых предложений
# Идёт по не числовым столбцам.
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

# Непосредственный запуск поиска
# raw_search = "Стол для рисования"
# search(raw_search, country_name = "", category = "", params = [])


######## Сортировка результата поиска
#TODO: Принимает на вход DF от функции find
'''
Сортировка результата поиска по приоритету для пользователя
По цене
По числу завершенных сделок
'''

######## Отображение отсортированного результата у Коли
'''
Функция search уже выдаёт результат по приоритету. Только не отсортированный по цене и т.д.
'''

######## Подсчёт полезных статистик для пользователя
'''
Код

'''

