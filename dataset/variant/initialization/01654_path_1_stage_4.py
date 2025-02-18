import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
solar_power = np.array([30, 45, 70, 100, 150, 225, 320, 430, 560, 700, 850])

# Sort the data in ascending order
sorted_indices = np.argsort(solar_power)
sorted_years = years[sorted_indices]
sorted_solar_power = solar_power[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

# Define new color scheme
new_color = '#1f77b4'  # A common matplotlib color for a change

# Plot sorted solar power as a bar chart
ax.bar(sorted_years, sorted_solar_power, color=new_color)

# Titles and labels
ax.set_title('Solar Generation Soars:\nOrdered Output from 2010 to 2020', fontsize=16, pad=20)
ax.set_xlabel('Chronological Period', fontsize=12)
ax.set_ylabel('Gigawatt Hours Produced', fontsize=12)

# Customize the x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 901, 100))

# Annotate each bar with its value
for i, y_solar in enumerate(sorted_solar_power):
    ax.text(sorted_years[i], y_solar + 20, f'{y_solar}', ha='center', fontsize=9, color=new_color)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()