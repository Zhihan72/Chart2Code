import matplotlib.pyplot as plt
import numpy as np

# Data: Plant-based food consumption in kilotons
years = np.array([2000, 2005, 2010, 2015, 2020])
north_america = np.array([50, 80, 120, 180, 250])
europe = np.array([40, 70, 110, 160, 220])
asia = np.array([20, 40, 80, 130, 200])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each region's data
ax.plot(years, north_america, marker='o', linestyle='-', color='blue', linewidth=2)
ax.plot(years, europe, marker='s', linestyle='--', color='green', linewidth=2)
ax.plot(years, asia, marker='^', linestyle='-.', color='red', linewidth=2)

# Title and labels
ax.set_title('Trendy Veggie Eats (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Chrono Year', fontsize=12)
ax.set_ylabel('Kilo Meals', fontsize=12)

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 301, 50))

# Annotate key points with the exact consumption values
for year, na, eu, as_ in zip(years, north_america, europe, asia):
    ax.annotate(f'{na}', (year, na), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{eu}', (year, eu), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{as_}', (year, as_), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
plt.show()