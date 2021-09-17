import math
import matplotlib.pyplot as plt

# Comprimentos dos pendulos
L = [63.0, 78.0, 88.5, 99.2, 111.5, 125.2, 139.1, 152.4, 163.9, 227.2]

# Tempo de 10 oscilações
t10 = [16.03, 17.97, 19.13, 20.18, 21.44, 22.72, 23.94, 25.03, 25.91, 30.28]

# Periodo T
T = [1.603, 1.797, 1.913, 2.018, 2.144, 2.272, 2.394, 2.503, 2.591, 3.028]

# T² (Período ao quadrado)
T2 = [x**2 for x in T]


x = L
y = T2
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

DeltaA = DeltaY/dabot
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

g = (4 * math.pi**2)/a
print(f"Valor calculado para g: {g}")

DeltaG = (4 * (math.pi**2) * DeltaA)/ (a**2)
print(f"Valor de Delta G: {DeltaG}")

# Plotar o gráfico
# Reta ideal
plt.plot(L, [a*x + b for x in L], "-", c="red", label="Melhor reta")
# Intervalo dispersao Y
plt.plot(L, [a*x + b + DeltaY for x in L], "--", c="black", alpha=0.3)
plt.plot(L, [a*x + b - DeltaY for x in L], "--", c="black", alpha=0.3, label="Intervalo de ajuste da reta")
# Pontos do grafico
plt.scatter(L, T2, c="blue", s=10)
# Configuracoes
plt.grid()
plt.xlabel("L")
plt.ylabel("T²")
plt.legend()
plt.show()

