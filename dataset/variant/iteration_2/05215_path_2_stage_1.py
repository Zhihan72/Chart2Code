import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Define data for different renewable energy technologies (adoption rate in percentage)
solar = [5, 7, 10, 14, 18, 23, 29, 35, 42, 50, 58]
wind = [4, 6, 9, 13, 17, 22, 27, 33, 40, 47, 55]
hydro = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Create subplots
fig, ax1 = plt.subplots(figsize=(16, 9))

# Line plots for each technology
ax1.plot(years, solar, marker='o', linestyle='-', color='#FF8C00', linewidth=2, label='Solar')
ax1.plot(years, wind, marker='s', linestyle='--', color='#1E90FF', linewidth=2, label='Wind')
ax1.plot(years, hydro, marker='^', linestyle='-.', color='#32CD32', linewidth=2, label='Hydro')

# Adding titles and labels
ax1.set_title('Adoption Trend of Renewable Energy Technologies (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Adoption Rate (%)', fontsize=14)

# Setting x-axis ticks
ax1.set_xticks(years)

# Adding grid lines
ax1.grid(visible=True, linestyle='--', alpha=0.6)

# Adding legend
ax1.legend(title='Technologies', loc='upper left', fontsize=12)

# Adding annotations
ax1.annotate('Solar Power Surges', xy=(2018, 42), xytext=(2017, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='#FF8C00')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()