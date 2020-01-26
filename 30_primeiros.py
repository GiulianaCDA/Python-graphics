import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("a2_MANCHAS.csv")
dataset = dataset.head(30)
plt.style.use('seaborn-dark')

x = dataset.Ano
y = dataset.manchas

plt.plot(x, y, color = '#2aad5c', linewidth = 3, marker="o")
plt.title('MANCHAS SOLARES EM WOLFER', fontsize=12, color = '#2aad5c')
plt.xlabel('ANO',  color = '#2aad5c', fontsize=10, position=[1,1])
plt.ylabel('MANCHAS', color = '#2aad5c', fontsize=10, position=[1,1])
plt.xticks(x, dataset.Ano, rotation = 'vertical')
plt.grid(True, linewidth=0)

plt.show()
#plt.savefig("30_primeiros.jpg")#
