import matplotlib.pyplot as plt
import numpy as np

fruits = ["Bananas", "Cherries", "Dates", "Apples", "Elderberries"]
production_volume = [1800, 950, 1130, 2500, 750]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFFF00', '#DA70D6']  # Tomato, SteelBlue, LimeGreen, Yellow, Orchid

fig, ax = plt.subplots(figsize=(10, 6))

# Creating a horizontal bar chart using barh
bars = ax.barh(fruits, production_volume, color=colors, edgecolor='black')

# Assigning text labels for each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 50, bar.get_y() + bar.get_height() / 2,
            f'{int(width)} tons', va='center', ha='left', fontsize=10, color='black')

ax.set_xlabel('Production Volume (tons)', fontsize=12)
ax.set_title('Top Fruit Production in Wonderland (2022)', fontsize=16, pad=20)
ax.set_xlim(0, max(production_volume) + 300)

plt.tight_layout()
plt.show()