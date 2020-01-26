import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("a2_MANCHAS.csv")
dataset = dataset.head(30)
plt.style.use('seaborn')

x = dataset.Ano
y = dataset.manchas

plt.boxplot(y, patch_artist = True)
plt.title('MANCHAS SOLARES EM WOLFER', fontsize=12, color = '#2e7ebf')

plt.grid('true', linewidth=0)

plt.show()
#plt.savefig("boxplot.jpg")#
