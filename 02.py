from matplotlib import pyplot as plt
import pandas as pd

cities = pd.read_csv("ctr.csv")


plt.scatter(cities["longitude"],cities["latitude"],s=cities["population"]/1000)
plt.show()