import numpy as np
import matplotlib.pyplot as plt

# Data for each year from 2000 to 2020
years = np.arange(2000, 2021)

# Numerical data corresponding to each fruit
mango = np.array([5, 7, 8, 10, 14, 18, 22, 30, 40, 52, 65, 80, 98, 115, 135, 150, 170, 195, 220, 245, 270])
pineapple = np.array([4, 5, 6, 7, 9, 10, 12, 15, 18, 22, 27, 32, 40, 45, 50, 55, 62, 70, 78, 85, 92])
banana = np.array([6, 8, 10, 14, 18, 22, 28, 35, 42, 50, 60, 70, 85, 95, 110, 125, 140, 160, 182, 200, 225])
coconut = np.array([2, 3, 4, 5, 6, 7, 9, 11, 14, 17, 21, 25, 30, 35, 42, 50, 58, 68, 78, 88, 100])

# Assembling data for the boxplot
plantation_data = np.vstack([mango, pineapple, banana, coconut])

# Create subplots
fig, ax = plt.subplots(figsize=(16, 10))

# Label for each type of fruit
fruit_labels = ['Mango', 'Pineapple', 'Banana', 'Coconut']
boxplot_data = np.transpose(plantation_data)

# Configuration and display of the boxplot
ax.boxplot(boxplot_data, vert=False, patch_artist=True,
           boxprops=dict(facecolor="#f08080", color="darkblue"),
           whiskerprops=dict(color="darkblue", linestyle="--"),
           capprops=dict(color="darkblue"),
           flierprops=dict(markerfacecolor='g', marker='*', markersize=8, color="darkblue"),
           medianprops=dict(color="red", linestyle="-."))

# Adding gridlines and changing grid style
ax.grid(True, linestyle=':', linewidth=0.7, color='gray')

# Modifying border visibility
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Setting new y-tick labels
ax.set_yticklabels(fruit_labels)
ax.set_title("Fruit Plantation Distribution in Tropical Bay (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Plantation Area (Hectares)', fontsize=14)
ax.set_ylabel('Fruit Type', fontsize=14)

# Adjust layout for the plot
plt.tight_layout()
plt.show()