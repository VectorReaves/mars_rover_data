import matplotlib.pyplot as plt
import pandas as pd


air_temperature = pd.read_csv('DATA/mars_temp_august_2021.csv')

plt.title("Mars Rover Air Temperature for August", fontsize=13)
plt.plot(air_temperature.DATE, air_temperature.Max, air_temperature.Min, linewidth=1)

plt.show()
