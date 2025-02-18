import matplotlib.pyplot as plt
import numpy as np

# Fruits and their (shuffled) production volumes in tons
fruits = ["Bananas", "Cherries", "Dates", "Apples", "Elderberries"]
production_volume = [1800, 950, 1130, 2500, 750]

# Color palette for each fruit
colors = ['#F0E68C', '#FFC0CB', '#D2691E', '#FFA07A', '#8A2BE2']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the vertical bar chart
bars = ax.bar(fruits, production_volume, color=colors, edgecolor='black', width=0.6)

# Add data labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 50,
            f'{int(height)} tons', ha='center', va='bottom', fontsize=10, color='black')

# Customize the appearance
ax.set_ylabel('Production Volume (tons)', fontsize=12, fontweight='bold')
ax.set_title('Top Fruit Production in Wonderland (2022)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, max(production_volume) + 300)
ax.set_xticks(np.arange(len(fruits)))
ax.set_xticklabels(fruits, fontsize=11, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations to highlight specific points
ax.annotate('Highest Volume', xy=(3, production_volume[3]), 
            xytext=(3.5, production_volume[3] + 300), 
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='red')

ax.annotate('Lowest Volume', xy=(4, production_volume[4]), 
            xytext=(4, production_volume[4] + 300), 
            arrowprops=dict(facecolor='blue', shrink=0.05),
            fontsize=10, fontweight='bold', color='blue')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()