import matplotlib.pyplot as plt
import numpy as np

# Years of data collection
years = np.arange(1990, 2022, 5)

# Artificial data for renewable energy sources in terawatt-hours (TWh)
# Removed 'Tidal' data
renewable_energy_data = {
    'Solar': np.array([2, 5, 10, 18, 30, 50, 80]),
    'Wind': np.array([1, 3, 7, 14, 25, 40, 65]),
    'Biomass': np.array([5, 8, 12, 17, 22, 28, 35])
}

# Recalculate total renewable energy excluding 'Tidal'
total_renewable_energy = np.sum(list(renewable_energy_data.values()), axis=0)

# Hypothetical total energy capacity potential on EcoIsland in TWh
total_energy_potential = 200

# Plotting the stacked area chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax1.stackplot(years, renewable_energy_data.values(), labels=renewable_energy_data.keys(), 
              colors=['#FFD700', '#87CEFA', '#32CD32'], alpha=0.8)
              
# Add title and labels
ax1.set_title('The Quest for Sustainable Energy: Evolution of Renewables on EcoIsland (1990-2020)', 
              fontsize=18, fontweight='bold', ha='center')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

# Secondary y-axis for total energy consumption as a percentage of potential
ax2 = ax1.twinx()
total_energy_percentage = (total_renewable_energy / total_energy_potential) * 100
ax2.plot(years, total_energy_percentage, color='purple', linestyle='--', marker='o', linewidth=2, label='Energy Potential Utilization (%)')
ax2.set_ylabel('Total Energy Utilization (%)', fontsize=14)

# Adding legend
ax1.legend(loc='upper left', title='Energy Sources', fontsize=12, title_fontsize='13')
ax2.legend(loc='upper right', fontsize=12)

# Annotate significant milestones
milestones = {
    2000: (total_energy_percentage[2], '20% Utilization'),
    2015: (total_energy_percentage[5], '70% Utilization'),
    2020: (total_energy_percentage[6], '85% Utilization')
}
for year, (percent, text) in milestones.items():
    ax2.annotate(f'{text}', xy=(year, percent), xycoords='data', 
                 xytext=(5, -25), textcoords='offset points',
                 arrowprops=dict(facecolor='black', arrowstyle='->'), 
                 fontsize=10, color='purple')

# Enhanced grid settings for clarity
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display plot
plt.show()