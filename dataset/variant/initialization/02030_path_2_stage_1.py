import matplotlib.pyplot as plt
import numpy as np

# Data for the eco-friendly beverage production
beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]
colors = ['#8FD14F', '#FFD700', '#FF69B4', '#40E0D0', '#BA55D3']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(beverages, production_volumes, color=colors, alpha=0.85, edgecolor='black')

# Adding data annotations on each bar
for bar, volume in zip(bars, production_volumes):
    xval = bar.get_width()
    ax.text(xval + 1, bar.get_y() + bar.get_height() / 2, f'{volume}M', va='center', ha='left', fontsize=11, fontweight='bold')

# Title and labels
ax.set_title("Eco-Friendly Beverage Production\nA Year in Review", fontsize=16, fontweight='bold')
ax.set_xlabel("Production Volume (Million Liters)", fontsize=14)
ax.set_ylabel("Beverage Type", fontsize=14)

# Adding a legend to highlight the most produced beverage
most_produced_index = np.argmax(production_volumes)
ax.legend([bars[most_produced_index]], [beverages[most_produced_index]], title="Top Producer", loc='lower right', fontsize=10, frameon=False)

# Grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()