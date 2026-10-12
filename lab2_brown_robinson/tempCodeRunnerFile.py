import numpy as np
import matplotlib.pyplot as plt

def brown_robinson(matrix, num_iterations=10, plot=False):
    A = np.array(matrix)
    m, n = A.shape
    
    p_strategy = 0
    q_strategy = 0
    
    x = np.zeros(m)
    y = np.zeros(n)
    
    p_counts = np.zeros(m)
    q_counts = np.zeros(n)
    
    upper_bounds = []
    lower_bounds = []
    approx_values = []
    
    if not plot:
        print(f"{'Крок':<5} | {'Стр. 1':<6} | {'Стр. 2':<6} | {'Нижня оцінка':<13} | {'Верхня оцінка':<13} | {'Наближена ціна'}")
        print("-" * 75)
    
    for k in range(1, num_iterations + 1):
        p_counts[p_strategy] += 1
        q_counts[q_strategy] += 1
        
        x += A[:, q_strategy]
        y += A[p_strategy, :]
        
        v_lower = np.min(y) / k
        v_upper = np.max(x) / k
        v_approx = (v_lower + v_upper) / 2
        
        upper_bounds.append(v_upper)
        lower_bounds.append(v_lower)
        approx_values.append(v_approx)
        
        if not plot and k <= 10:
             print(f"{k:<5} | {p_strategy+1:<6} | {q_strategy+1:<6} | {v_lower:<13.3f} | {v_upper:<13.3f} | {v_approx:.3f}")
        
        p_strategy = np.argmax(x)
        q_strategy = np.argmin(y)
        
    p_opt = p_counts / num_iterations
    q_opt = q_counts / num_iterations
    
    if not plot:
        print("\n--- Результати після", num_iterations, "ітерацій ---")
        print("Змішана стратегія Гравець 1:", np.round(p_opt, 3))
        print("Змішана стратегія Гравець 2:", np.round(q_opt, 3))
        print("Наближена ціна гри:", round(approx_values[-1], 3))

    # Побудова графіка збіжності
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, num_iterations + 1), upper_bounds, label='Верхня оцінка', color='red', linewidth=1.5)
        plt.plot(range(1, num_iterations + 1), lower_bounds, label='Нижня оцінка', color='blue', linewidth=1.5)
        plt.plot(range(1, num_iterations + 1), approx_values, label='Наближена ціна', color='green', linestyle='--')
        plt.title('Збіжність методу Брауна-Робінсон (Фіктивний розіграш)')
        plt.xlabel('Номер ітерації')
        plt.ylabel('Оцінка ціни гри')
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.show()

# Задана матриця згідно з варіантом №5 (розмірність 4x3, значення [-4; 5])
A = [
    [5, -2, 3],
    [-1, 4, -3],
    [0, 1, 2],
    [2, -4, 5]
]

brown_robinson(A, num_iterations=10, plot=False)

# Запуск для візуалізації збіжності на великій вибірці (1000 ітерацій)
brown_robinson(A, num_iterations=1000, plot=True)