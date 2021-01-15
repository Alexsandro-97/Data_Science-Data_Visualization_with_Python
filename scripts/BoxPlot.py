#BoxPlot - Diagrama de de caixa
import matplotlib.pyplot as plt 
import random

vetor = []

for i in range(1000):
    num = random.randint(0,500)
    vetor.append(num)

plt.boxplot(vetor)
plt.title("BoxPlot")
plt.show()