import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the 21st century, global interest in plant-based foods has surged. Let's visualize the growth of plant-based food consumption from 2000 to 2020 in different regions: North America, Europe, Asia, and Oceania. This script will generate a line chart to showcase the consumption trend over the years.

# Data: Plant-based food consumption in kilotons
years = np.array([2000, 2005, 2010, 2015, 2020])
north_america = np.array([50, 80, 120, 180, 250])
europe = np.array([40, 70, 110, 160, 220])
asia = np.array([20, 40, 80, 130, 200])
oceania = np.array([15, 35, 70, 100, 150])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each region's data
ax.plot(years, north_america, marker='o', linestyle='-', color='blue', linewidth=2, label='North America')
ax.plot(years, europe, marker='s', linestyle='--', color='green', linewidth=2, label='Europe')
ax.plot(years, asia, marker='^', linestyle='-.', color='red', linewidth=2, label='Asia')
ax.plot(years, oceania, marker='d', linestyle=':', color='purple', linewidth=2, label='Oceania')

# Title and labels
ax.set_title('Surge in Plant-Based Food Consumption\nacross Various Global Regions (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Consumption (Kilotons)', fontsize=12)

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 301, 50))

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Add a grid for better readability
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate key points with the exact consumption values
for year, na, eu, as_, oc in zip(years, north_america, europe, asia, oceania):
    ax.annotate(f'{na}', (year, na), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{eu}', (year, eu), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{as_}', (year, as_), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{oc}', (year, oc), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()