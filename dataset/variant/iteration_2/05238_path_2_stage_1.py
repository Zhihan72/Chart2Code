import matplotlib.pyplot as plt
import numpy as np

# Fruits and their production volumes in tons
fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
production_volume = [2500, 1800, 950, 1130, 750]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the vertical bar chart with a single color
bars = ax.bar(fruits, production_volume, color='#FFA07A', edgecolor='black', width=0.6)

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
ax.annotate('Highest Volume', xy=(0, production_volume[0]), 
            xytext=(0.5, production_volume[0] + 300), 
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='red')

ax.annotate('Lowest Volume', xy=(4, production_volume[4]), 
            xytext=(4, production_volume[4] + 300), 
            arrowprops=dict(facecolor='blue', shrink=0.05),
            fontsize=10, fontweight='bold', color='blue')

# Adjust layout to ensure the chart is visually appealing
plt.tight_layout()

# Display the plot
plt.show()