import matplotlib.pyplot as plt
import numpy as np

# Data (in kilograms)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
apples_consumption = [180, 130, 150, 220]  # Randomly altered
bananas_consumption = [200, 80, 150, 100]  # Randomly altered
oranges_consumption = [110, 140, 120, 180] # Randomly altered

# Aggregate data
data = [apples_consumption, bananas_consumption, oranges_consumption]

# Define labels for the x-axis and for the fruits
fruits = ['Apples', 'Bananas', 'Oranges']

# Number of seasons and fruits
n_seasons = len(seasons)
n_fruits = len(fruits)

# Define the positions of the bars
x = np.arange(n_seasons)
bar_width = 0.25

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each fruit's consumption as a separate set of bars
colors = ['#FF6347', '#FFD700', '#FFA500']
for i, fruit in enumerate(fruits):
    bars = ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i], label=fruit)
    
    # Add text labels above the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9)

# Add labels and title
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Fruit Consumption (kg)', fontsize=12)
ax.set_title('Annual Fruit Consumption Trends in a Village', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(x + bar_width * (n_fruits - 1) / 2)
ax.set_xticklabels(seasons)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0)

# Add a legend
ax.legend(title='Fruits', fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()