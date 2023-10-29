import numpy as np
from scipy.optimize import minimize

# Функція, яку ми мінімізуємо
def objective(x):
    x1, x2, lambda1, lambda2 = x
    return 3 * x1**2 - x1 * x2 + x2**2 - 23 * x1 - 9 * x2 + 10

# Обмеження - обидва обмеження нерівності повинні бути задоволені
def constraint1(x):
    return 5 * x[0]**2 + 5 * x[1] + 22

def constraint2(x):
    return 10 * x[0] - 5 * x[1] - 37

# Початкові значення для змінних та множників Лагранжа
x0 = [0, 0, 0, 0]

# Обмеження нерівності - обидва обмеження повинні бути менше або рівні 0
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
cons = [con1, con2]

# Мінімізація функції з обмеженнями
result = minimize(objective, x0, constraints=cons)

# Вивід результатів
x_optimal = result.x[:2]  # Оптимальні значення x та y
optimal_value = result.fun  # Оптимальне значення функції
lambda1 = result.x[2]  # Значення множника Лагранжа lambda1
lambda2 = result.x[3]  # Значення множника Лагранжа lambda2

print("Оптимальні значення x і y:", x_optimal)
print("Оптимальне значення функції:", optimal_value)
print("Множник Лагранжа lambda1:", lambda1)
print("Множник Лагранжа lambda2:", lambda2)
