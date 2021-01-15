#Gráfico de Disperção
import matplotlib.pyplot as plt

x = ['Janeiro', 'Março', 'Junho', 'Agosto', 'Outubro']
y = [2, 3, 7, 1, 0]
z = [350, 550, 650, 750, 800]

titulo = "Gráfico de Scatterplot: gráfico de disperção"
eixox = "Mês referente ao ano 2019"
eixoy = "Valor"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = "Faturamento", color = 'g', marker = '.', s = z)
plt.plot(x, y, color = '#000080', linestyle = '-', linewidth = 5)
plt.legend()
plt.show()
#plt.savefig("GraficoDispercao.pdf")