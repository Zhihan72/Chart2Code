import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the growth and impact of renewable energy investments in fictional countries from 2000 to 2020.
years = np.arange(2000, 2021, 4)
countries = ['Solaria', 'Ventura', 'Hydrona', 'Geotherma']

# Data: Investment in renewable energy (in billion dollars) for each country
solaria_investment = [5, 10, 15, 25, 35, 50]
ventura_investment = [3, 8, 12, 20, 30, 40]
hydrona_investment = [2, 7, 10, 15, 25, 35]
geotherma_investment = [1, 4, 7, 10, 17, 25]

# Data: Impact of renewable energy investments (in percentage contribution to total energy)
solaria_impact = [1, 5, 10, 20, 35, 50]
ventura_impact = [2, 4, 8, 15, 25, 40]
hydrona_impact = [0.5, 3, 6, 10, 20, 30]
geotherma_impact = [0.2, 2, 5, 8, 15, 25]

# Creating the figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# First subplot: Line chart of investments over years
ax1.plot(years, solaria_investment, marker='o', linestyle='-', color='#FF6347', linewidth=2, label='Solaria')
ax1.plot(years, ventura_investment, marker='s', linestyle='--', color='#4682B4', linewidth=2, label='Ventura')
ax1.plot(years, hydrona_investment, marker='^', linestyle='-.', color='#32CD32', linewidth=2, label='Hydrona')
ax1.plot(years, geotherma_investment, marker='D', linestyle=':', color='#FFD700', linewidth=2, label='Geotherma')

ax1.set_title('Renewable Energy Investment Growth (2000-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Investment (Billion Dollars)', fontsize=14)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)
ax1.legend(title='Countries', loc='best', fontsize=12)

# Annotating specific points
ax1.annotate('Solaria Boom', xy=(2016, 35), xytext=(2008, 40),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#FF6347')
ax1.annotate('Ventura Surge', xy=(2020, 40), xytext=(2012, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#4682B4')

# Second subplot: Line chart of impact on total energy
ax2.plot(years, solaria_impact, marker='o', linestyle='-', color='#FF6347', linewidth=2, label='Solaria')
ax2.plot(years, ventura_impact, marker='s', linestyle='--', color='#4682B4', linewidth=2, label='Ventura')
ax2.plot(years, hydrona_impact, marker='^', linestyle='-.', color='#32CD32', linewidth=2, label='Hydrona')
ax2.plot(years, geotherma_impact, marker='D', linestyle=':', color='#FFD700', linewidth=2, label='Geotherma')

ax2.set_title('Impact of Renewable Energy on Total Energy (2000-2020)', fontsize=16, weight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Energy Contribution (%)', fontsize=14)
ax2.set_xticks(years)
ax2.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)
ax2.legend(title='Countries', loc='best', fontsize=12)

# Annotating specific points
ax2.annotate('Solaria Breakthrough', xy=(2020, 50), xytext=(2012, 55),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#FF6347')
ax2.annotate('Geotherma Increment', xy=(2020, 25), xytext=(2012, 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#FFD700')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()