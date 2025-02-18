import matplotlib.pyplot as plt
import numpy as np

# Updated data for the pie chart with additional made-up data series
power_distribution = [25, 20, 15, 10, 10, 20, 8, 12, 5]

# Updated pie chart with new series and colors
fig, ax1 = plt.subplots(figsize=(8, 8))
ax1.pie(power_distribution, autopct='%1.1f%%', startangle=90, 
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'], 
        explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0))

plt.show()