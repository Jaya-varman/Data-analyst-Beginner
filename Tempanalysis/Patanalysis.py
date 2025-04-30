import matplotlib.pyplot as plt

import pandas as pd

myfile=pd.read_csv("temperatures.csv")


plt.plot(myfile['YEAR'], myfile['ANNUAL'])
plt.title("Average Monthly Temperature in India (Year-wise)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
