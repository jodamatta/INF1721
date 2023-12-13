def knapsack_10(B, n, weights, values):
    # Inicializar uma tabela de memoização para armazenar os resultados intermediários
    opt = [[0] * (B + 1) for _ in range(n + 1)]

    # Preencher a tabela usando a equação de recorrência
    for i in range(1, n + 1):
        for b in range(B + 1):
            opt[i][b] = opt[i - 1][b]
            for j in range(1, min(11, b // weights[i - 1] + 1)):
                opt[i][b] = max(opt[i][b], opt[i - 1][b - j * weights[i - 1]] + j * values[i - 1])

    # Reconstruir a solução ótima
    selected_items = []
    i, b = n, B
    while i > 0 and b > 0:
        if opt[i][b] != opt[i - 1][b]:
            selected_items.append((i, min(10, b // weights[i - 1])))
            b -= min(10, b // weights[i - 1]) * weights[i - 1]
        i -= 1

    return opt[n][B], selected_items
