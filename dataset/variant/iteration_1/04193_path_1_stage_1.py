import matplotlib.pyplot as plt
import numpy as np

# Data (in kilograms)
apples_consumption = [150, 220, 180, 130]
bananas_consumption = [100, 200, 150, 80]
oranges_consumption = [120, 180, 140, 110]

# Aggregate data
data = [apples_consumption, bananas_consumption, oranges_consumption]

# Number of seasons
n_seasons = 4

# Define the positions of the bars
x = np.arange(n_seasons)
bar_width = 0.25

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each fruit's consumption as a separate set of bars
colors = ['#FF6347', '#FFD700', '#FFA500']
for i in range(3):
    bars = ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i])
    
    # Remove text labels above the bars

# Remove labels and title
# ax.set_xlabel('Seasons', fontsize=12)
# ax.set_ylabel('Fruit Consumption (kg)', fontsize=12)
# ax.set_title('Annual Fruit Consumption Trends in a Village', fontsize=16, fontweight='bold', pad=15)
# ax.set_xticks(x + bar_width * (n_fruits - 1) / 2)
# ax.set_xticklabels(seasons)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0)

# Remove legend
# ax.legend(title='Fruits', fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()