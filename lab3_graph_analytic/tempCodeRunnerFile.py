import numpy as np
import matplotlib.pyplot as plt

def plot_2xn(matrix, title):
    A = np.array(matrix)
    x = np.linspace(0, 1, 500)
    plt.figure(figsize=(10, 6))
    lines = []
    
    for j in range(A.shape[1]):
        y = A[0, j] * x + A[1, j] * (1 - x)
        lines.append(y)
        plt.plot(x, y, label=f'Стратегія B{j+1}', linewidth=1.5)
        
    lower_envelope = np.min(lines, axis=0)
    plt.plot(x, lower_envelope, color='black', linewidth=4, label='Нижня обвідна', alpha=0.6)
    
    max_idx = np.argmax(lower_envelope)
    opt_x = x[max_idx]
    opt_v = lower_envelope[max_idx]
    
    plt.scatter([opt_x], [opt_v], color='red', s=100, zorder=5, 
                label=f'Оптимум: x={opt_x:.3f}, v={opt_v:.3f}')
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Імовірність x (Стратегія A1)', fontsize=12)
    plt.ylabel('Виграш 1-го гравця (v)', fontsize=12)
    plt.xlim(0, 1)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_mx2(matrix, title):
    A = np.array(matrix)
    y_prob = np.linspace(0, 1, 500)
    plt.figure(figsize=(10, 6))
    lines = []
    
    for i in range(A.shape[0]):
        x_val = A[i, 0] * y_prob + A[i, 1] * (1 - y_prob)
        lines.append(x_val)
        plt.plot(y_prob, x_val, label=f'Стратегія A{i+1}', linewidth=1.5)
        
    upper_envelope = np.max(lines, axis=0)
    plt.plot(y_prob, upper_envelope, color='black', linewidth=4, label='Верхня обвідна', alpha=0.6)
    
    min_idx = np.argmin(upper_envelope)
    opt_y = y_prob[min_idx]
    opt_v = upper_envelope[min_idx]
    
    plt.scatter([opt_y], [opt_v], color='red', s=100, zorder=5, 
                label=f'Оптимум: y={opt_y:.3f}, v={opt_v:.3f}')
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Імовірність y (Стратегія B1)', fontsize=12)
    plt.ylabel('Програш 2-го гравця (v)', fontsize=12)
    plt.xlim(0, 1)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Виклик функцій для 4 матриць
A1 = [[0, 2, 1, 5], [-14, 5, -3, -5]]
A2 = [[5, -14, 2, 0], [-3, 5, -1, 3]]
A3 = [[-14, 10], [5, 5], [0, 2]]
A4 = [[5, -14], [-5, 5], [2, -1]]

plot_2xn(A1, "Матриця 1 (2x4) із сідловою точкою")
plot_2xn(A2, "Матриця 2 (2x4) без сідлової точки")
plot_mx2(A3, "Матриця 3 (3x2) із сідловою точкою")
plot_mx2(A4, "Матриця 4 (3x2) без сідлової точки")