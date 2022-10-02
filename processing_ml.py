# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 22:12:05 2022

@author: Vasily
"""

import pickle
import heapq

"""
Все файлы можно найти тут : https://drive.google.com/drive/folders/16fyjPa11u3phBI_q7QgK2ShKlltEh91r?usp=sharing
"""
# Выдаёт по запросу 10 наиболее подходящих категорий nkpd2_code
# Использует нейронную сеть.

# Указать путь к обученной модели
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb')) # Файл нужно загрузить заранее, чтобы работало быстро!

def codes_search(loaded_model, text):
    # prediction = loaded_model.predict([text])
    prediction_proba = loaded_model.predict_proba([text])

    code_probs = heapq.nlargest(10, prediction_proba[0])
    find_codes = []
    for code in code_probs:
        for i in range(len(prediction_proba[0])):
            if prediction_proba[0][i] == code: find_codes.append(loaded_model.classes_[i])
    return find_codes #list

for i in range(5):
    print(f"Запрос {i}")
    print(codes_search(loaded_model, text=input()))
    # сдвоенная шестерня
    # ['28.15.24.130', '33.12.16.000', '28.11.4', '28.15.24.131', '45.20.11.211', '28.15.22.000', '95.11.10.190', '45.20.21.111', '28.92.62.000', '28.92.12.130']

