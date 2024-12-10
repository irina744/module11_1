import data
import requests
import numpy as np
import matplotlib.pyplot as plt

url = 'https://urban-university.ru'

response = requests.get(url)

if response.status_code == 200:
    print("Ответ получен успешно.")
    print(response.text)
else:
    print(f"Произошла ошибка при получении данных. Код статуса: {response.status_code}")


random_array = np.random.randint(0, 100, size=20)
mean_value = np.mean(random_array)
print('Массив случайных чисел: ', random_array)
print('Среднее значение: ', mean_value)

month = np.arange(1, 13)
passengers = np.random.randint(50, 300, size=len(month))

plt.figure(figsize=(10, 6))
plt.plot(month, passengers, marker='o', linestyle='-')
plt.title('Количество пассажиров по месяцам в 1958 году')
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()







