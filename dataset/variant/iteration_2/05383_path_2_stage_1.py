import matplotlib.pyplot as plt
import numpy as np

# Data: Plant-based food consumption in kilotons
years = np.array([2000, 2005, 2010, 2015, 2020])
north_america = np.array([50, 80, 120, 180, 250])
europe = np.array([40, 70, 110, 160, 220])
asia = np.array([20, 40, 80, 130, 200])
oceania = np.array([15, 35, 70, 100, 150])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each region's data
ax.plot(years, north_america, marker='o', linestyle='-', color='blue', linewidth=2, label='Group A')
ax.plot(years, europe, marker='s', linestyle='--', color='green', linewidth=2, label='Group B')
ax.plot(years, asia, marker='^', linestyle='-.', color='red', linewidth=2, label='Group C')
ax.plot(years, oceania, marker='d', linestyle=':', color='purple', linewidth=2, label='Group D')

# Title and labels
ax.set_title('Trendy Veggie Eats (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Chrono Year', fontsize=12)
ax.set_ylabel('Kilo Meals', fontsize=12)

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