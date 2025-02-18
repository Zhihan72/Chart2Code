import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are analyzing how different types of fruits have been used across various consumer products over the last five years.
# This will help understand trends and preferences in the consumer market for fruit-based products.
years = np.array([2018, 2019, 2020, 2021, 2022])
fruit_types = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Data representing the number of times each fruit type has been used in various consumer products over the years
usage_data = np.array([
    [150, 160, 170, 180, 190],  # Apple
    [140, 135, 150, 160, 155],  # Banana
    [50, 55, 60, 65, 80],       # Cherry
    [40, 45, 50, 55, 70],       # Date
    [30, 35, 40, 45, 60]        # Elderberry
])

# Create a figure with subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Generate bar width
bar_width = 0.15

# Positions for each bar corresponding to each year
positions = [np.arange(len(years))]
for _ in range(1, len(fruit_types)):
    positions.append([p + bar_width for p in positions[-1]])

# Colors for each fruit type
colors = ['#e74c3c', '#f1c40f', '#8e44ad', '#16a085', '#3498db']

# Plot each fruit type data
for i, fruit in enumerate(fruit_types):
    ax.bar(positions[i], usage_data[i], bar_width, alpha=0.8, label=fruit, color=colors[i])

# Set labels, title, and ticks
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage Instances', fontsize=12)
ax.set_title('Fruit Usage in Consumer Products Over 5 Years', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years)
ax.legend(title='Fruit Types', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the bar chart
plt.show()