# Файл для преобразования датасетов к формату, по которому будет производиться поиск

# Тест открытия полного датасета
import pandas as pd
import numpy as np
import re

# Тест открытия полных версий датасетов
# Для повторения и финального деплоя на сервер нужно будет
# Добавить в папку datasets папку data c полными версиями датасетов (3 .csv файла)


# df_contract = pd.read_csv('datasets/data/Контракты 44ФЗ.csv', sep=';')
# df_guide = pd.read_csv('datasets/data/Справочник пром производства.csv', sep=';')
df_offer = pd.read_csv('datasets/data/Ценовые предложения поставщиков.csv', sep=';')


# Поиск товара

df_offer = df_offer.replace(np.nan, 'none')      # заменяем все значени Nan на строки

df_dict = df_offer.drop(['price', 'inn', 'okpd2_code','country_code'], axis=1).to_dict('records')  # отбросим ненужные для поиска столбцы и запишеи DataFrame в словарь

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
          elif first: priority[i] += 1   # Если продукт уже добавлен - повышаем приоритет
    for k, p in priority.items():
        if p < max(priority.values()): out.pop(k)   # Оставляем товары с лучшим совпадением
    return(out)


response = find(df_offer, df_dict, 'Лук')
print(response)


'''
Дальше, что делаем

Глеб - разделение предобработки и поиска на 2 разных файла
- Обсудить с Колей
Как с фронтедна вызывать функцию поиска.

'''

