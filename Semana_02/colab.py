import matplotlib.pyplot as plt

# Dados do monitor serial (X, Y1, Y2)
dados = [
    (4825, 5.00, 0.00),
    (5227, 4.76, 0.24),
    (5629, 4.39, 0.61),
    (6032, 4.05, 0.95),
    (6433, 3.74, 1.26),
    (6836, 3.45, 1.55),
    (7238, 3.19, 1.81),
    (7641, 2.94, 2.06),
    (8043, 2.71, 2.29),
    (8444, 2.50, 2.50),
    (8847, 2.31, 2.69),
    (9249, 2.13, 2.87),
    (9652, 1.96, 3.04),
    (10054, 1.81, 3.19),
    (10457, 1.67, 3.33),
    (10858, 1.54, 3.46),
    (11260, 1.42, 3.58),
    (11663, 1.31, 3.69),
    (12065, 1.21, 3.79),
    (12468, 1.12, 3.88),
    (12870, 1.03, 3.97),
    (13273, 0.95, 4.05),
    (13675, 0.88, 4.12),
    (14077, 0.81, 4.19),
    (14480, 0.75, 4.25),
    (14881, 0.69, 4.31),
    (15284, 0.64, 4.36),
    (15686, 0.59, 4.41),
    (16089, 0.54, 4.46),
    (16491, 0.50, 4.50),
    (16893, 0.46, 4.54),
    (17296, 0.43, 4.57),
    (17698, 0.39, 4.61)
]

# Separando os dados
x = [item[0] for item in dados]
y1 = [item[1] for item in dados]
y2 = [item[2] for item in dados]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y1, 'o-', label='Y1 (Curva 1)')
plt.plot(x, y2, 'o-', label='Y2 (Curva 2)')

# Configurando rótulos e título
plt.xlabel('X (Unidade de medida)')
plt.ylabel('Valores')
plt.title('Gráfico de Dispersão - Dados do Monitor Serial')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
