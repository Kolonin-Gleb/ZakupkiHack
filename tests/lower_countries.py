import pandas as pd

test = pd.read_csv('G:\GitHub repos\ZakupkiHack\datasets\country_directory.csv', on_bad_lines='skip', sep=';')

test['country_name'] = [c_n.lower() for c_n in test['country_name']]

print(test)

test.to_csv("lower_countries.csv", index=False, sep=';')

