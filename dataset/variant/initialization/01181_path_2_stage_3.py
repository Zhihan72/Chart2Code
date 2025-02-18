import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]
coffee_consumption = [3.0, 5.0, 2.2, 4.5, 3.4]  # Additional data series for coffee

# Creating a bar width offset
bar_width = 0.35
y_pos = np.arange(len(countries))

# Creating horizontal bar chart for tea consumption
fig, ax = plt.subplots(figsize=(10, 6))

# Plot tea consumption bars
tea_bars = ax.barh(y_pos, tea_consumption, color='#A0522D', alpha=0.8, height=bar_width, label='Tea')

# Plot coffee consumption bars on the same chart
coffee_bars = ax.barh(y_pos + bar_width, coffee_consumption, color='#8B4513', alpha=0.8, height=bar_width, label='Coffee')

# Add data annotations for tea
for bar in tea_bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2.0,
            f'{width:.1f}', va='center', ha='left', fontsize=10)

# Add data annotations for coffee
for bar in coffee_bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2.0,
            f'{width:.1f}', va='center', ha='left', fontsize=10)

# Set the title and labels
ax.set_title('Average Annual Beverage Consumption\nPer Person by Country', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Country', fontsize=12)
ax.set_xlabel('Consumption (kg/person/year)', fontsize=12)

# Set y-axis tick positions and labels
ax.set_yticks(y_pos + bar_width / 2)
ax.set_yticklabels(countries, fontsize=10)

# Adding grid only on x-axis for better readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Include legend
ax.legend()

# Adjust layout
plt.tight_layout()

# Show the chart
plt.show()