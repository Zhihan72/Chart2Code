import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy generation values in GW
solar = [1.2, 1.6, 2.0, 2.8, 3.5, 4.2, 5.1, 6.3, 7.4, 8.6, 9.8]
wind = [2.5, 3.0, 3.8, 4.5, 5.1, 5.8, 6.3, 7.0, 7.8, 9.0, 10.2]
hydro = [8.1, 8.2, 8.4, 8.5, 8.7, 8.9, 9.0, 9.2, 9.3, 9.5, 9.7]
geothermal = [0.4, 0.6, 0.8, 0.9, 1.0, 1.1, 1.3, 1.5, 1.6, 1.8, 2.0]

# Define a single color for all energy sources
single_color = '#ff7f0e'

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source using the same color
ax.plot(years, solar, label='Solar', color=single_color, marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, wind, label='Wind', color=single_color, marker='s', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, hydro, label='Hydro', color=single_color, marker='^', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, geothermal, label='Geothermal', color=single_color, marker='d', linestyle='-', linewidth=2, markersize=8)

# Customize the plot
ax.set_title("Renewable Energy Generation in EcoVille (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Energy Generation (GW)", fontsize=14)
ax.set_xticks(years)
ax.legend(title='Energy Sources', fontsize=12, loc='upper left')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Annotate significant event: Major solar farm established in 2015
ax.annotate('Major Solar Farm Established', xy=(2015, 4.2), xytext=(2013, 6),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()