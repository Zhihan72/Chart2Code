import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
power_distribution = [25, 20, 15, 10, 10, 20]

# Create a single subplot figure
fig, ax1 = plt.subplots(figsize=(8, 8))

# Pie chart plot
ax1.pie(power_distribution, autopct='%1.1f%%', startangle=90, 
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], 
        explode=(0.1, 0, 0, 0, 0, 0))

plt.show()