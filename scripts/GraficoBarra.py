#Gráfico de barra
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 11, 7, 9, 4]

titulo = "Gráfico de Barra"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()
#plt.savefig("GraficoBarra.pdf")