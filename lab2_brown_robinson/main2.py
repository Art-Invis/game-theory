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

    
    if plot:
        iterations = np.arange(1, num_iterations + 1)

        fig, ax = plt.subplots(figsize=(12, 7))

        ax.plot(
            iterations, upper_bounds,
            color='red', linewidth=2,
            marker='o', markersize=6,
            markerfacecolor='white',
            markeredgewidth=1.5,
            label='Верхня оцінка ціни гри'
        )

        ax.plot(
            iterations, lower_bounds,
            color='royalblue', linewidth=2,
            marker='s', markersize=6,
            markerfacecolor='white',
            markeredgewidth=1.5,
            label='Нижня оцінка ціни гри'
        )

        # Наближена ціна гри
        ax.plot(
            iterations, approx_values,
            color='green', linewidth=2,
            linestyle='--',
            marker='D', markersize=5,
            label='Наближена ціна гри'
        )

        # Виділення останньої ітерації
        ax.scatter(
            iterations[-1], approx_values[-1],
            color='darkgreen', s=110,
            edgecolors='black', zorder=5,
            label=f'Результат останньої ітерації: '
                  f'{approx_values[-1]:.3f}'
        )

        
        if num_iterations <= 20:
            for i, value in enumerate(approx_values):
                ax.annotate(
                    f'{value:.3f}',
                    (iterations[i], value),
                    textcoords='offset points',
                    xytext=(0, 9),
                    ha='center',
                    fontsize=9,
                    color='darkgreen'
                )

        ax.set_title(
            'Збіжність методу Брауна—Робінсон\n'
            f'Кількість ітерацій: {num_iterations}',
            fontsize=15, fontweight='bold', pad=16
        )
        ax.set_xlabel('Номер ітерації N', fontsize=12)
        ax.set_ylabel('Оцінка ціни гри', fontsize=12)

        if num_iterations <= 20:
            ax.set_xticks(iterations)

        ax.grid(True, which='major', linestyle=':', alpha=0.65)
        ax.axhline(0, color='black', linewidth=0.8, alpha=0.5)

        ax.legend(
            loc='best',
            fontsize=10,
            frameon=True,
            framealpha=0.95
        )

        ax.margins(x=0.06, y=0.18)

        fig.tight_layout()
        plt.show()



# Матриця виграшів для варіанта №5
# Розмірність 3x4, значення в межах [-4; 5]

A = [
    [5, -1,  0,  2],
    [-2, 4,  1, -4],
    [3, -3,  2,  5]
]

brown_robinson(A, num_iterations=10, plot=False)

brown_robinson(A, num_iterations=10, plot=True)



