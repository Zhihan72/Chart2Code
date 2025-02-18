import matplotlib.pyplot as plt
import numpy as np

fruits = ["Bananas", "Cherries", "Dates", "Apples", "Elderberries"]
production_volume = [1800, 950, 1130, 2500, 750]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFFF00', '#DA70D6']  # Tomato, SteelBlue, LimeGreen, Yellow, Orchid

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(fruits, production_volume, color=colors, edgecolor='black')

ax.set_xlim(0, max(production_volume) + 300)

plt.tight_layout()
plt.show()