import math

def calculate_cooperative_game():
    # Вхідні дані варіанту №5
    V = {
        (1,): 1300, (2,): 1400, (3,): 1700,
        (1, 2): 3000, (1, 3): 3400, (2, 3): 3600,
        (1, 2, 3): 5600
    }
    
    print("--- 1. ПЕРЕВІРКА СУПЕРАДИТИВНОСТІ ТА ІСТОТНОСТІ ---")
    sum_individual = V[(1,)] + V[(2,)] + V[(3,)]
    is_essential = sum_individual < V[(1, 2, 3)]
    print(f"Сума виграшів поодинці: {sum_individual}")
    print(f"Виграш великої коаліції: {V[(1, 2, 3)]}")
    print(f"Гра є істотною: {is_essential}")
    
    print("\n--- 2. 0-1 СПРОЩЕНА ФОРМА ---")
    K = V[(1, 2, 3)] - sum_individual
    V_prime = {
        (1,): 0.0, (2,): 0.0, (3,): 0.0,
        (1, 2): (V[(1, 2)] - (V[(1,)] + V[(2,)])) / K,
        (1, 3): (V[(1, 3)] - (V[(1,)] + V[(3,)])) / K,
        (2, 3): (V[(2, 3)] - (V[(2,)] + V[(3,)])) / K,
        (1, 2, 3): 1.0
    }
    for k, v in V_prime.items():
        print(f"V'{k} = {v:.4f}")

    print("\n--- 3. ВЕКТОР ШЕПЛІ ---")
    n = 3
    players = [1, 2, 3]
    shapley = {1: 0, 2: 0, 3: 0}
    
    # Розрахунок граничного внеску гравця в коаліції
    for i in players:
        phi_i = 0
        for S, v_s in V.items():
            if i in S:
                s_len = len(S)
                S_without_i = tuple(x for x in S if x != i)
                v_s_without_i = V.get(S_without_i, 0)
                
                weight = (math.factorial(s_len - 1) * math.factorial(n - s_len)) / math.factorial(n)
                phi_i += weight * (v_s - v_s_without_i)
        shapley[i] = phi_i
        print(f"Виграш гравця {i} (Ф_{i}): {phi_i:.2f}")

    print(f"Сума вектора Шеплі: {sum(shapley.values()):.2f}")
    
    print("\n--- 4. ПЕРЕВІРКА НАЛЕЖНОСТІ С-ЯДРУ ---")
    checks = [
        shapley[1] >= V[(1,)], shapley[2] >= V[(2,)], shapley[3] >= V[(3,)],
        shapley[1] + shapley[2] >= V[(1, 2)],
        shapley[1] + shapley[3] >= V[(1, 3)],
        shapley[2] + shapley[3] >= V[(2, 3)]
    ]
    print(f"Всі умови С-ядра виконуються: {all(checks)}")

calculate_cooperative_game()

