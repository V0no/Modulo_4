import matplotlib.pyplot as plt

# Seus dados (tempo, valor1, valor2)
dados = [
    (0, 5.00, 0.00),
    (401, 4.80, 0.20),
    (803, 4.61, 0.39),
    (578026, 0.02, 4.98),
    (578426, 0.02, 4.98),
    (578828, 0.02, 4.98),
    (579229, 0.02, 4.98),
    (579630, 0.02, 4.98),
    (580031, 0.02, 4.98),
    (580432, 0.02, 4.98),
    (580834, 0.02, 4.98),
    (581234, 0.01, 4.99),
    (581636, 0.02, 4.98),
    (582037, 0.01, 4.99)
]

# Separando os dados
x = [item[0] for item in dados]
y1 = [item[1] for item in dados]
y2 = [item[2] for item in dados]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Y1 (Valor 1)', marker='o')
plt.plot(x, y2, label='Y2 (Valor 2)', marker='x')

# Configurando rótulos e título
plt.xlabel('Tempo (ms)')
plt.ylabel('Valores')
plt.title('Gráfico de Dados do Monitor Serial')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
