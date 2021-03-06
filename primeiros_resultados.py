import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("a2_MANCHAS.csv")
dataset = dataset.head(10)

x = dataset.Ano
y = dataset.manchas
plt.style.use('seaborn-dark')
plt.plot(x, y, color = '#524f9c', linewidth = 3)
plt.title('MANCHAS SOLARES EM WOLFER', fontsize=12, color = '#524f9c')
plt.xlabel('ANO',  color = '#524f9c', fontsize=10)
plt.ylabel('MANCHAS', color = '#524f9c', fontsize=10)
plt.xticks(x, dataset.Ano, rotation = 'vertical')
plt.grid(True, linewidth=0)

plt.show()
#plt.savefig("primeiros_resultados.jpg")#
