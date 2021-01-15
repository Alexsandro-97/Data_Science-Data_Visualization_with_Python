#Gráfico de linha
import matplotlib.pyplot as plt

x = [1, 2]
y = [2, 3]

titulo = "Gráfico de Linha"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y)
plt.show()
#plt.savefig("GraficoLinha.pdf")
