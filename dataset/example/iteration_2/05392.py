import matplotlib.pyplot as plt
import numpy as np

# Define the years and months for x-axis
years = np.arange(2010, 2021)

# Create data for bacterial strains' concentration over a decade
e_coli = np.array([5, 15, 30, 45, 60, 50, 40, 35, 25, 20, 15])  # Rapid growth, then decline
staph = np.array([10, 20, 25, 40, 55, 60, 65, 70, 75, 80, 85])  # Steady growth
salmonella = np.array([8, 12, 18, 22, 30, 38, 45, 55, 65, 75, 80])  # Accelerated growth

# Total concentration data to normalize the values if needed
total_concentration = e_coli + staph + salmonella

# Plot configuration and chart creation
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()  # Create a secondary y-axis.

# Create area plot
ax1.stackplot(years, e_coli, staph, salmonella, labels=['E. coli', 'Staph', 'Salmonella'], 
              colors=['#ff9999','#66b3ff','#99ff99'], alpha=0.7)

# Create a line plot on the same figure for the total concentration
ax2.plot(years, total_concentration, label='Total Bacterial Concentration', color='black', lw=2, linestyle='--', marker='o')

# Titles and labels
ax1.set_title('Bacterial Strain Concentration in Water Bodies (2010-2020)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Individual Bacterial Concentration (CFU/mL)', fontsize=14, color='dimgray')
ax2.set_ylabel('Total Bacterial Concentration (CFU/mL)', fontsize=14, color='dimgray')

# Grid and legend
ax1.grid(True, linestyle='--', alpha=0.5, color='gray')
ax1.legend(loc='upper left', fontsize=12, title='Strain')
ax2.legend(loc='upper right', fontsize=12, title='Total Concentration')

# Highlight key events and milestones
events = [(2012, 'New Water Treatment Plant Opens'), (2018, 'Industrial Waste Regulation Applied')]
for year, event in events:
    ax1.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax1.annotate(event, xy=(year, 140), xytext=(year, 150),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                 fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()