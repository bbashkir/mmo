import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('clock.csv')

# Первичный анализ данных
print("Размер датасета:", df.shape)
#display(df.head())

# Проверка пропущенных значений
print(df.isnull().sum())

# Предобработка данных
# Замена ERROR на NaN в столбце Sleep Duration (hours)
df.loc[df['Sleep Duration (hours)'] == "ERROR", 'Sleep Duration (hours)'] = np.nan

# Замена Very High на 10 в столбце Stress Level
df.loc[df['Stress Level'] == "Very High", 'Stress Level'] = 10

# Преобразование типов данных
df['Sleep Duration (hours)'] = df['Sleep Duration (hours)'].astype(float)
df['Stress Level'] = df['Stress Level'].astype(float)

# Заполнение пропущенных значений средним значением по столбцу
columns_to_fill = ['Sleep Duration (hours)', 'Stress Level']
for col in columns_to_fill:
    mean_value = df[col].mean()
    df[col] = df[col].fillna(mean_value)

df['Stress Level'] = df['Stress Level'].astype(int)

# Группировка по уровню активности
activity_group = df.groupby('Activity Level').mean()
print(activity_group)

# Гистограмма для уровня кислорода в крови
plt.figure(figsize=(12, 6))
sns.histplot(df['Blood Oxygen Level (%)'], bins=30, kde=True, color='orange')
plt.title('Распределение уровня кислорода в крови', fontsize=16)
plt.xlabel('Уровень кислорода в крови (%)', fontsize=14)
plt.ylabel('Количество пользователей', fontsize=14)
plt.show()

# Boxplot для уровня стресса
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Stress Level'], color='purple')
plt.title('Boxplot для уровня стресса', fontsize=16)
plt.xlabel('Уровень стресса', fontsize=14)
plt.show()

# Анализ распределения данных
plt.figure(figsize=(12, 6))
sns.histplot(df['Heart Rate (BPM)'], bins=50, kde=True, color='skyblue')
plt.title('Распределение частоты сердечных сокращений', fontsize=16)
plt.xlabel('Частота сердечных сокращений (BPM)', fontsize=14)
plt.ylabel('Количество пользователей', fontsize=14)
plt.show()

# Гистограмма для уровня стресса
plt.figure(figsize=(12, 6))
sns.histplot(df['Stress Level'], bins=10, kde=True, color='lightgreen')
plt.title('Распределение уровня стресса', fontsize=16)
plt.xlabel('Уровень стресса', fontsize=14)
plt.ylabel('Количество пользователей', fontsize=14)
plt.show()

# Диаграмма рассеяния: Частота сердечных сокращений vs. Уровень стресса
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Heart Rate (BPM)'], y=df['Stress Level'], alpha=0.5)
plt.title('Диаграмма рассеяния: Частота сердечных сокращений vs. Уровень стресса')
plt.xlabel('Частота сердечных сокращений (BPM)')
plt.ylabel('Уровень стресса')
plt.show()