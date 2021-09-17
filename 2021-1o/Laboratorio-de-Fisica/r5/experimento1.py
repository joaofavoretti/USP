import math
import matplotlib.pyplot as plt

####################################
# Pontos utilizados no gráfico

# Comprimento da mola
L = [0.403, 0.605, 0.900, 1.067, 1.305, 1.492, 1.71, 1.938, 2.16, 2.378]

# Massas
m = [0.01023, 0.03114, 0.05941, 0.07548, 0.09871, 0.11606, 0.13827, 0.1592, 0.18095, 0.20227]

# Peso relativo à massa
P = [x*9.81 for x in m]

# Definicao de eixo X e Y que será calculado no MMQ
x = L
y = P

####################################
# Calcular os valores do MMQ

# Media de x
MediaX = 0
for i in x:
    MediaX += i
MediaX /= len(x)
print(f"Media de X: {MediaX}")

# Media de y
MediaY = 0
for i in y:
    MediaY += i
MediaY /= len(y)
print(f"Media de Y: {MediaY}")

# Valor de a
atop = 0
abot = 0
for i in range(len(x)):
    atop += (x[i] - MediaX)*y[i]
    abot += (x[i] - MediaX)**2
a = atop/abot
print(f"Valor do coeficiente angular: {a}")

# Valor de b
b = MediaY - a*MediaX
print(f"Valor do coeficiente linear: {b}")

# Dispersao media do ajuste (delta y)
dytop = 0
for i in range(len(x)):
    dytop += (a*x[i]+b-y[i])**2

DeltaY = math.sqrt(dytop/(len(x) - 2))
print(f"Dispersão média do ajuste: {DeltaY}")

# Incerteza do coeficiente angular (delta a)
dabot = 0
for i in x:
    dabot += (i-MediaX)**2

DeltaA = DeltaY/math.sqrt(dabot)
print(f"Incerteza do coeficiente angular: {DeltaA}")

# Incerteza do coeficiente linear (delta b)
dbtop = 0
dbbot = 0
for i in x:
    dbtop += i**2
    dbbot += (i-MediaX)**2
dbbot *= len(x)

DeltaB = (math.sqrt(dbtop/dbbot))*DeltaY
print(f"Incerteza do coeficiente linear: {DeltaB}")

####################################
# Lugar para calcular valores baseado nos parametros do MMQ
print()
print(f"Constante elástica K: {a}")
print(f"Comprimento inicial da mola L0: {-b/a}")
print()

####################################
# Plotar o gráfico

# Reta ideal
plt.plot(L, [a*x + b for x in L], "-", c="red", label="Melhor reta")
# Intervalo dispersao Y
plt.plot(L, [a*x + b + DeltaY for x in L], "--", c="black", alpha=0.3)
plt.plot(L, [a*x + b - DeltaY for x in L], "--", c="black", alpha=0.3, label="Intervalo de ajuste da reta")
# Pontos do grafico
plt.scatter(x, y, c="blue", s=10)
# Configuracoes
plt.grid()
plt.xlabel("L")
plt.ylabel("P")
plt.legend()
plt.show()
