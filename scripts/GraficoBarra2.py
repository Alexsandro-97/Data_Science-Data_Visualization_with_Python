#Gráfico de barras 2
import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 11, 7, 9, 4]

x2 = [2, 4, 6, 8, 10]
y2 = [4, 13, 9, 4, 6]

titulo = "Comparando gráficos de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo1")
plt.bar(x2, y2, label = "Grupo2")
plt.legend()
plt.show()
#plt.savefig("GraficoBarra2.pdf")