#Crescimento da população brasileira de (1980-2016) - DataSUS
import matplotlib.pyplot as plt

dados = open("data/populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
  if i != 0:
      linha = dados[i].split(";")
      x.append(int(linha[0]))
      y.append(int(linha[1]))

plt.bar(x, y, color = "gray")
plt.plot(x, y, color = "black", linewidth = 3, linestyle = "solid")
plt.title("Crescimento da população brasileira(1980-2016)")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")
plt.show()
#plt.savefig("EstudoDeCaso.pdf")