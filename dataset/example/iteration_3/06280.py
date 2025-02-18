import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Our thematic visualization this time focuses on the evolution of renewable energy
# production (in terawatt-hours) for three countries: Country A, Country B, and Country C
# over a span of 40 years. The focus is to show how each country's renewable energy
# sector has progressed over the years and to provide insights on their growth trends.

# Time period (years)
years = np.array(range(1980, 2020, 5))

# Renewable energy production data (in terawatt-hours)
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])
country_b_production = np.array([2, 12, 25, 60, 90, 140, 210, 275])
country_c_production = np.array([1, 5, 15, 35, 60, 105, 180, 240])

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the line charts for renewable energy production
ax.plot(years, country_a_production, marker='o', linestyle='-', linewidth=2, color='green', label='Country A')
ax.plot(years, country_b_production, marker='s', linestyle='-', linewidth=2, color='blue', label='Country B')
ax.plot(years, country_c_production, marker='^', linestyle='-', linewidth=2, color='orange', label='Country C')

# Annotations for energy production
for i, (a, b, c) in enumerate(zip(country_a_production, country_b_production, country_c_production)):
    ax.text(years[i], a + 5, f'{a}TWh', ha='center', fontsize=9, color='darkgreen', fontweight='bold')
    ax.text(years[i], b - 12, f'{b}TWh', ha='center', fontsize=9, color='darkblue', fontweight='bold')
    ax.text(years[i], c + 5, f'{c}TWh', ha='center', fontsize=9, color='orangered', fontweight='bold')

# Title and labels
plt.title("Renewable Energy Production Over Time\nFor Three Countries (1980-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (Terawatt-hours)", fontsize=14)

# Legends
ax.legend(title='Countries', fontsize=10, loc='upper left')

# Grid lines for readability
ax.grid(True, linestyle='-', alpha=0.3)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()