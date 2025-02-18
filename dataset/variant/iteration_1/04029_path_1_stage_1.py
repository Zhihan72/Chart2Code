import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# CO2 emissions data in million metric tons
energy = [400, 385, 370, 350, 330, 310, 290, 270, 250, 230, 215]
transport = [300, 295, 285, 275, 260, 245, 230, 215, 200, 185, 170]
industry = [250, 245, 240, 230, 220, 210, 200, 190, 180, 170, 160]
agriculture = [150, 148, 145, 142, 138, 132, 125, 118, 112, 108, 100]
total_emissions = np.array(energy) + np.array(transport) + np.array(industry) + np.array(agriculture)

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Shuffle the assigned colors for each data group or type
ax1.stackplot(years, energy, transport, industry, agriculture,
              labels=['Energy', 'Transport', 'Industry', 'Agriculture'],
              colors=['#66b3ff', '#99ff99', '#ff9999', '#ffcc99'], alpha=0.7)

# Plot total emissions on the secondary y-axis
ax2.plot(years, total_emissions, 'k--', label='Total CO2 Emissions (MMT)', linewidth=2)

# Add annotations for each year on total emissions plot
for i, value in enumerate(total_emissions):
    ax2.annotate(f'{value}', (years[i], total_emissions[i]),
                 textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8)

# Enhance plot with title, labels, and legend
ax1.set_title('Reduction of CO2 Emissions per Sector (2015 - 2025)',
              fontsize=18, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 Emissions by Sector (MMT)', fontsize=14)
ax2.set_ylabel('Total CO2 Emissions (MMT)', fontsize=14)

# Customize tick parameters
ax1.tick_params(axis='x', labelrotation=45)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Add grid for better readability
ax1.grid(visible=True, linestyle='--', linewidth=0.5, color='gray', which='both')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()