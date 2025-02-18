import matplotlib.pyplot as plt
import numpy as np

# Time period (years)
years = np.array(range(1980, 2020, 5))

# Renewable energy production data (in terawatt-hours)
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])
country_b_production = np.array([2, 12, 25, 60, 90, 140, 210, 275])
country_c_production = np.array([1, 5, 15, 35, 60, 105, 180, 240])

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the line charts for renewable energy production
ax.plot(years, country_a_production, marker='o', linestyle='-', linewidth=2, color='green')
ax.plot(years, country_b_production, marker='s', linestyle='-', linewidth=2, color='blue')
ax.plot(years, country_c_production, marker='^', linestyle='-', linewidth=2, color='orange')

# Annotations for energy production
for i, (a, b, c) in enumerate(zip(country_a_production, country_b_production, country_c_production)):
    ax.text(years[i], a + 5, f'{a}TWh', ha='center', fontsize=9, color='darkgreen', fontweight='bold')
    ax.text(years[i], b - 12, f'{b}TWh', ha='center', fontsize=9, color='darkblue', fontweight='bold')
    ax.text(years[i], c + 5, f'{c}TWh', ha='center', fontsize=9, color='orangered', fontweight='bold')

# Title and labels
plt.title("Renewable Energy Production Over Time\nFor Three Countries (1980-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (Terawatt-hours)", fontsize=14)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()