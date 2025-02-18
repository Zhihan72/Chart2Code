import matplotlib.pyplot as plt
import numpy as np

# Species names
species = ['Oak Trees', 'Pine Trees', 'Maple Trees', 'Deer Population', 'Bird Population']

# Years
years = np.array([2020, 2021, 2022, 2023, 2024])

# Growth data (in arbitrary units)
oak_growth = np.array([100, 120, 140, 160, 180])
pine_growth = np.array([90, 105, 130, 150, 170])
maple_growth = np.array([80, 95, 115, 135, 155])
deer_growth = np.array([50, 60, 70, 85, 95])
bird_growth = np.array([200, 220, 260, 300, 340])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each species growth
ax.plot(years, oak_growth, marker='o', linestyle='-', color='#8A2BE2', linewidth=2, label='Oak Trees')
ax.plot(years, pine_growth, marker='s', linestyle='--', color='#FFA500', linewidth=2, label='Pine Trees')
ax.plot(years, maple_growth, marker='^', linestyle='-.', color='#00FF00', linewidth=2, label='Maple Trees')
ax.plot(years, deer_growth, marker='D', linestyle=':', color='#FF4500', linewidth=2, label='Deer Population')
ax.plot(years, bird_growth, marker='*', linestyle='-', color='#1E90FF', linewidth=2, label='Bird Population')

# Title and labels
ax.set_title('Ecosystem Balance: Annual Growth Rates of Various Species in Evergreen Forest (2020-2024)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Growth Rate (Arbitrary Units)', fontsize=12)

# Grid and ticks
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_xticks(years)
ax.tick_params(axis='both', which='major', labelsize=10)

# Legend
ax.legend(title='Species', fontsize=10, title_fontsize='13', loc='upper left')

# Annotating final growth values
for growth, label, color in zip([oak_growth, pine_growth, maple_growth, deer_growth, bird_growth], 
                                ['Oak Trees', 'Pine Trees', 'Maple Trees', 'Deer Population', 'Bird Population'], 
                                ['#8A2BE2', '#FFA500', '#00FF00', '#FF4500', '#1E90FF']):
    ax.annotate(f'{growth[-1]}',
                xy=(years[-1], growth[-1]),
                xytext=(-10, 5),
                textcoords='offset points',
                fontsize=10,
                color=color,
                arrowprops=dict(arrowstyle='->', lw=1.5))

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()