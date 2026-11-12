import numpy as np
from scipy.optimize import linprog

# Перетворена матриця A' (після додавання K=5)
A_prime = np.array([
    [10, 3, 8, 5],
    [4,  9, 2, 6],
    [5,  6, 7, 1]
])
K = 5

# --- Пряма задача (Перший гравець) ---
c_p1 = [1, 1, 1]
A_ub_p1 = -A_prime.T
b_ub_p1 = [-1, -1, -1, -1]

res_p1 = linprog(c_p1, A_ub=A_ub_p1, b_ub=b_ub_p1, bounds=(0, None), method='highs')
x_opt = res_p1.x
Z_min = res_p1.fun

# Розрахунок V' та стратегій P
V_prime_p1 = 1 / Z_min
V_p1 = V_prime_p1 - K
p_opt = x_opt * V_prime_p1

# --- Двоїста задача (Другий гравець) ---
c_p2 = [-1, -1, -1, -1]
A_ub_p2 = A_prime
b_ub_p2 = [1, 1, 1]

res_p2 = linprog(c_p2, A_ub=A_ub_p2, b_ub=b_ub_p2, bounds=(0, None), method='highs')
y_opt = res_p2.x
F_max = -res_p2.fun

# Розрахунок V' та стратегій Q
V_prime_p2 = 1 / F_max
V_p2 = V_prime_p2 - K
q_opt = y_opt * V_prime_p2

# --- Вивід результатів ---
print(f"Оптимальні значення x: {[round(val, 4) for val in x_opt]}")
print(f"Мінімум цільової функції Z: {Z_min:.4f}")
print(f"Змішана стратегія p*: {[round(val, 4) for val in p_opt]}")
print(f"Ціна гри V: {V_p1:.4f}\n")

print(f"Оптимальні значення y: {[round(val, 4) for val in y_opt]}")
print(f"Максимум цільової функції F: {F_max:.4f}")
print(f"Змішана стратегія q*: {[round(val, 4) for val in q_opt]}")
print(f"Ціна гри V: {V_p2:.4f}")

