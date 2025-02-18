import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Fictional data for energy production in Terawatt-hours (TWh)
solar = [10, 14, 21, 30, 38, 50, 68, 80, 92, 110, 130]
wind = [50, 58, 70, 85, 97, 110, 128, 140, 155, 170, 190]
hydro = [300, 305, 310, 312, 315, 320, 322, 325, 328, 330, 332]
geothermal = [3, 4, 6, 8, 10, 12, 15, 18, 19, 21, 23]

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line charts for each renewable energy source with altered styles
ax.plot(years, solar, label='Solar', color='orange', marker='p', linestyle='-.')
ax.plot(years, wind, label='Wind', color='royalblue', marker='x', linestyle='--')
ax.plot(years, hydro, label='Hydro', color='deepskyblue', marker='h', linestyle='-')
ax.plot(years, geothermal, label='Geothermal', color='saddlebrown', marker='*', linestyle=':')

# Adjust titles and labels
ax.set_title('Renewable Energy Production Trends (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Produced (TWh)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 400, 50))

# Alter the legend style and location
ax.legend(title='Energy Sources', fontsize=12, title_fontsize=13, loc='lower right')

# Adding annotations for significant milestones
annotations = [
    (2016, 50, 'Solar: 50 TWh'),
    (2020, 110, 'Wind: 190 TWh'),
    (2020, 332, 'Hydro: 332 TWh'),
    (2020, 23, 'Geothermal: 23 TWh')
]
for (year, output, text) in annotations:
    ax.annotate(text, xy=(year, output), xytext=(year - 2, output + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

# Modify grid style
ax.grid(linestyle=':', alpha=0.5)

# Modify border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()