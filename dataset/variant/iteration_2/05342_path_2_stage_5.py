import matplotlib.pyplot as plt
import numpy as np

hobbies = [
    "Photography", 
    "Writing", 
    "Crafting", 
    "Music", 
    "Gardening", 
    "Reading", 
    "Cooking/Baking", 
    "Gaming", 
    "Exercise"
]

percentages = [5, 8, 10, 15, 25, 30, 35, 40, 45]

# Different colors for variety
colors = ['lightcoral', 'turquoise', 'lightgreen', 'salmon', 'plum', 'darkorange', 'mediumpurple', 'gold', 'tomato']

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(hobbies, percentages, color=colors, edgecolor='navy')

# Alter marker types, set dashes for visibility
for i, bar in enumerate(bars):
    bar.set_hatch('/')

ax.set_ylim(0, 50)

# Add gridlines with a different style
ax.yaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.5)

# Altering border visibility by using spines to create a customized box around the plot
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_color('none')  # Removing the right spine
ax.spines['bottom'].set_color('darkgray')
ax.spines['left'].set_color('darkgray')

# Adding a legend with different location and style
ax.legend(['Hobbies'], loc='upper left', frameon=True, framealpha=0.8)

plt.show()