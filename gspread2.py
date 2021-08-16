import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(8,5))

air_temperature = pd.read_csv('DATA/mars_temp_august_2021.csv')

plt.title("Mars Rover Air Temperature for August", fontsize=13)
plt.plot(air_temperature.DATE, air_temperature.Max, 'b.-', label='Max', linewidth=2)
plt.plot(air_temperature.DATE, air_temperature.Min, 'r.-', label='Min')

# 'b.-' creates the dots on the line. Label='' creates the label on the top left corner of the graph.
plt.xlabel('Date') # This makes the label for the x axis.
plt.ylabel('Degrees in Fahrenheit')

plt.xticks(air_temperature.DATE)

plt.legend()

plt.show()
