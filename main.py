import pandas as pd
import matplotlib.pyplot as plt



data = {
    "name": ["Alex", "Nick", "Polly", "Kate", "Vlad"],
    "Math": [5, 2, 4, 3, 5],
    "Literature": [4, 3, 5, 2, 5],
    "Russian": [3, 4, 5, 5, 3],
    "History": [4, 4, 5, 5, 3],
    "Geography": [2, 3, 5, 4, 5]
}
#print('\n')
df = pd.DataFrame(data)
print(f'\n{df.head()}\n')


for subject in df.columns[1:]:
    print(f'{subject}: средний балл: {df[subject].mean()} '
                     f'медианная оценка: {df[subject].median()} '
                     f'Q1: {df[subject].quantile(0.25)} '
                     f'Q3: {df[subject].quantile(0.75)} '
                     f'IQR: {df[subject].quantile(0.75) - df[subject].quantile(0.25)} '
                     f'стандартное отклонение: {df[subject].std()}')

