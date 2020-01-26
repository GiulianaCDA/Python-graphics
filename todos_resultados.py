import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("a2_MANCHAS.csv")
plt.style.use('seaborn-dark')

x = dataset.Ano
y = dataset.manchas

plt.plot(x, y, color = '#eb807a', linewidth = 3)
plt.title('MANCHAS SOLARES EM WOLFER', fontsize=12, color = '#eb807a')
plt.xlabel('ANO',  color = '#eb807a', fontsize=10)
plt.ylabel('MANCHAS', color = '#eb807a', fontsize=10)
plt.grid(True, linewidth=0)

plt.show()
#plt.savefig("todos_resultados.png")#
