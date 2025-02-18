import matplotlib.pyplot as plt
import numpy as np

# Backstory: Solar Power Adoption Over Time
# The chart shows the monthly kWh produced from home solar systems in three different countries
# (Solarland, Ecotopia, and Sunstate) over a year, reflecting the adoption and efficiency of solar power systems.

# Data: Monthly kWh produced by home solar systems in three countries over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
solarland = np.array([120, 135, 150, 170, 190, 215, 240, 230, 210, 190, 160, 130])
ecotopia = np.array([80, 100, 120, 140, 160, 180, 200, 195, 175, 155, 130, 100])
sunstate = np.array([95, 110, 125, 145, 165, 185, 205, 200, 180, 160, 140, 115])

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot data for each country with different styles
ax.plot(months, solarland, label='Solarland', marker='o', linestyle='-', color='#FF5733', linewidth=2)
ax.plot(months, ecotopia, label='Ecotopia', marker='s', linestyle='-', color='#33FF57', linewidth=2)
ax.plot(months, sunstate, label='Sunstate', marker='^', linestyle='-', color='#3357FF', linewidth=2)

# Add a secondary axis for the aggregated monthly kWh produced
total_kWh = solarland + ecotopia + sunstate
ax2 = ax.twinx()
ax2.plot(months, total_kWh, label='Total kWh', color='gray', linestyle='--', linewidth=1.5)

# Annotate significant points for clarity
significant_months = [2, 6, 10]  # March, July, and November are notable
for i in significant_months:
    ax.annotate(f'{solarland[i]} kWh', xy=(months[i], solarland[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#FF5733')
    ax.annotate(f'{ecotopia[i]} kWh', xy=(months[i], ecotopia[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#33FF57')
    ax.annotate(f'{sunstate[i]} kWh', xy=(months[i], sunstate[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#3357FF')
    ax2.annotate(f'{total_kWh[i]} kWh', xy=(months[i], total_kWh[i]), xytext=(0, -20), textcoords='offset points', fontsize=9, color='gray')

# Titles and labels
ax.set_title('Solar Power Surge:\nMonthly Production of Home Solar Systems in Three Countries', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Monthly kWh Produced (Individual Countries)', fontsize=12)
ax2.set_ylabel('Total Monthly kWh Produced', fontsize=12, color='gray')

# Legends
ax.legend(loc='upper left', bbox_to_anchor=(0.05, 1), title='Countries')
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1), title='Aggregated')

# Grid and layout adjustments
ax.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()