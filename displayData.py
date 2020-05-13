from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

df = pd.read_csv('handData.csv')

outcomes = df['outcome'].value_counts().index.tolist()
counts = df['outcome'].value_counts().tolist()

plt.barh(outcomes, counts)

plt.tight_layout()

plt.show()
             
             