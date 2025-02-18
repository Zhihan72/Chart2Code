import matplotlib.pyplot as plt
import numpy as np

# Backstory: A comprehensive analysis of different breeds of dragons based on their mythical traits.

# Dragon attributes
attributes = ['Fire Power', 'Flying Speed', 'Stealth', 'Wisdom', 'Defense', 'Healing Power']
n_attributes = len(attributes)

# Data for each dragon breed
fire_dragon = [9, 8, 4, 7, 6, 5]
wind_dragon = [6, 10, 8, 6, 4, 7]
earth_dragon = [7, 5, 6, 8, 9, 10]
water_dragon = [5, 7, 8, 7, 6, 9]

# Append the first value to close the radar chart
for dragon in [fire_dragon, wind_dragon, earth_dragon, water_dragon]:
    dragon += dragon[:1]

# Calculate angles for each attribute
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the figure and axis for the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Plot each dragon's attribute data
colors = ['red', 'blue', 'green', 'purple']
dragon_names = ['Fire Dragon', 'Wind Dragon', 'Earth Dragon', 'Water Dragon']
dragon_data = [fire_dragon, wind_dragon, earth_dragon, water_dragon]

for idx, dragon in enumerate(dragon_data):
    ax.plot(angles, dragon, color=colors[idx], linewidth=2, linestyle='solid', label=dragon_names[idx])
    ax.fill(angles, dragon, color=colors[idx], alpha=0.25)

# Annotate the attributes
plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold', color='darkblue')

# Customize the radar chart background and grid
ax.set_facecolor('whitesmoke')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_yticklabels([])

# Add legend outside the plot to avoid overlap
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Dragon Breeds', fontsize=10)

# Set the title with a line break for better readability
plt.title('Mythical Dragon Traits Analysis\nComparative Overview of Different Breeds', size=16, fontweight='bold', pad=30, color='black')

# Adjust layout to prevent text from being cut off
plt.tight_layout()

# Display the radar chart
plt.show()