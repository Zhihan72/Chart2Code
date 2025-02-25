import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021, 4)
countries = ['Solaria', 'Ventura', 'Hydrona', 'Geotherma']

solaria_investment = [5, 10, 15, 25, 35, 50]
ventura_investment = [3, 8, 12, 20, 30, 40]
hydrona_investment = [2, 7, 10, 15, 25, 35]
geotherma_investment = [1, 4, 7, 10, 17, 25]

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Altered subplot with different styles
ax.plot(years, solaria_investment, marker='v', linestyle='--', color='#A0522D', linewidth=2.5, label='Solaria')
ax.plot(years, ventura_investment, marker='p', linestyle='-', color='#4682B4', linewidth=2.5, label='Ventura')
ax.plot(years, hydrona_investment, marker='x', linestyle=':', color='#556B2F', linewidth=2, label='Hydrona')
ax.plot(years, geotherma_investment, marker='*', linestyle='-.', color='#DAA520', linewidth=2, label='Geotherma')

ax.set_title('Renewable Energy Investment Growth (2000-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Investment (Billion Dollars)', fontsize=14)
ax.set_xticks(years)
ax.grid(True, linestyle='-.', which='both', color='lightgrey', alpha=0.7)  # Altered grid style
ax.legend(title='Countries', loc='upper left', fontsize=12)  # Altered legend position

# Altered annotations
ax.annotate('Solaria Boom', xy=(2016, 35), xytext=(2008, 45),
             arrowprops=dict(facecolor='#A0522D', arrowstyle='->'), fontsize=10, color='#A0522D')
ax.annotate('Ventura Surge', xy=(2020, 40), xytext=(2010, 50),
             arrowprops=dict(facecolor='#4682B4', arrowstyle='->'), fontsize=10, color='#4682B4')

# Show the plot
plt.tight_layout()
plt.show()