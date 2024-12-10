from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Создание массива чисел
arr = np.array([1, 2, 3, 4, 5])

# Вывод массива в консоль
print("Массив чисел:")
print(arr)

# Выполнение математических операций
print("\nСумма всех элементов массива:", np.sum(arr))
print("Среднее значение элементов массива:", np.mean(arr))
print("Максимальное значение в массиве:", np.max(arr))
print("Минимальное значение в массиве:", np.min(arr))

# Умножение всех элементов массива на 2
arr *= 2
print("\nМассив после умножения на 2:")
print(arr)

# загрузка изображение, измение размера, сохранение измененного изображения
image = Image.open('YZzxTz0hddU.jpg')
resized_image = image.resize((800, 900))
resized_image.save('resized_image.jpg')

#визуализация в виде графика
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()