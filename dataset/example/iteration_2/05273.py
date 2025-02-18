import matplotlib.pyplot as plt
import numpy as np

# Define years in the future timeline
years = np.arange(2040, 2051)

# Hypothetical global adoption rates of electric vehicles (EVs) in percentage
ev_adoption_rates = np.array([5, 7, 10, 15, 22, 30, 40, 50, 62, 75, 90])

# Hypothetical decrease in CO2 emissions due to EV adoption in million tons
co2_reduction = np.array([2, 3, 5, 9, 14, 20, 28, 35, 47, 60, 75])

# Hypothetical increase in renewable energy sources as part of total energy production in percentage
renewable_energy_share = np.array([18, 20, 22, 25, 29, 35, 42, 50, 58, 65, 75])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the global adoption rates of electric vehicles
ax1.plot(years, ev_adoption_rates, 'o-', linewidth=2, color='blue', label='EV Adoption (%)')

# Set primary y-axis (left)
ax1.set_xlabel('Years', fontsize=12)
ax1.set_ylabel('EV Adoption (%)', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Annotate data points for EV adoption rates
for i, rate in enumerate(ev_adoption_rates):
    ax1.annotate(f'{rate}%', (years[i], ev_adoption_rates[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color='blue')

# Create a secondary y-axis for CO2 reduction
ax2 = ax1.twinx()
ax2.plot(years, co2_reduction, 's--', linewidth=2, color='green', label='CO2 Reduction (Million Tons)')

# Set secondary y-axis (right) for CO2 reduction
ax2.set_ylabel('CO2 Reduction (Million Tons)', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Annotate data points for CO2 reduction
for i, reduction in enumerate(co2_reduction):
    ax2.annotate(f'{reduction} MT', (years[i], co2_reduction[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=10, color='green')

# Overlay another secondary y-axis for renewable energy share
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Offset right axis
ax3.plot(years, renewable_energy_share, 'd-.', linewidth=2, color='red', label='Renewable Energy Share (%)')

# Set tertiary y-axis (offset right) for renewable energy share
ax3.set_ylabel('Renewable Energy Share (%)', fontsize=12, color='red')
ax3.tick_params(axis='y', labelcolor='red')

# Annotate data points for renewable energy share
for i, share in enumerate(renewable_energy_share):
    ax3.annotate(f'{share}%', (years[i], renewable_energy_share[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color='red')

# Title and grid customization
plt.title('Global Transition to Sustainable Transport & Energy\n(2040 - 2050)', fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=12)

# Automatically adjust the layout
fig.tight_layout()

# Display the plot
plt.show()