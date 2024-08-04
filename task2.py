# Обчислення значення інтеграла функції методом Монте-Карло

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
def monte_carlo_integration(f, a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    area = (b - a) * np.mean(y_random)
    return area

# Кількість випадкових точок для методу Монте-Карло
num_samples = 100000

# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

# Обчислення точного інтегралу за допомогою quad
quad_result, _ = quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Точний результат (quad): {quad_result}")

# Генерація файлу Markdown з результатами
with open('results.md', 'w', encoding='utf-8') as file:
    file.write("# Результати інтегрування\n")
    file.write("## Функція для інтегрування\n")
    file.write("Функція: f(x) = x^2\n")
    file.write("## Межі інтегрування\n")
    file.write(f"Нижня межа: {a}\n")
    file.write(f"Верхня межа: {b}\n")
    file.write("## Результати обчислень\n")
    file.write(f"- Результат методу Монте-Карло: {monte_carlo_result}\n")
    file.write(f"- Точний результат (функція quad): {quad_result}\n")
    file.write("## Висновки\n")
    file.write("Метод Монте-Карло є наближеним і його точність залежить від кількості зразків. В даному випадку, різниця між результатами невелика.\n")
    file.write("## Графік функції\n")
    file.write("![Графік інтегрування](plot.png)\n")

# Створення графіка
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

# Збереження графіка
plt.savefig('plot.png')
plt.show()
