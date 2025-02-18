import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021, 4)
countries = ['SolariX', 'VenturiZ', 'HydrioW', 'GeoThermY']

solaria_investment = [5, 10, 15, 25, 35, 50]
ventura_investment = [3, 8, 12, 20, 30, 40]
hydrona_investment = [2, 7, 10, 15, 25, 35]
geotherma_investment = [1, 4, 7, 10, 17, 25]

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Altered subplot with different styles
ax.plot(years, solaria_investment, marker='v', linestyle='--', color='#A0522D', linewidth=2.5, label='SolariX')
ax.plot(years, ventura_investment, marker='p', linestyle='-', color='#4682B4', linewidth=2.5, label='VenturiZ')
ax.plot(years, hydrona_investment, marker='x', linestyle=':', color='#556B2F', linewidth=2, label='HydrioW')
ax.plot(years, geotherma_investment, marker='*', linestyle='-.', color='#DAA520', linewidth=2, label='GeoThermY')

ax.set_title('Energinvestment Evolution (2000-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Funds (Billion $)', fontsize=14)
ax.set_xticks(years)
ax.grid(True, linestyle='-.', which='both', color='lightgrey', alpha=0.7)
ax.legend(title='Regions', loc='upper left', fontsize=12)

# Altered annotations
ax.annotate('SolariX Surge', xy=(2016, 35), xytext=(2008, 45),
             arrowprops=dict(facecolor='#A0522D', arrowstyle='->'), fontsize=10, color='#A0522D')
ax.annotate('VenturiZ Peak', xy=(2020, 40), xytext=(2010, 50),
             arrowprops=dict(facecolor='#4682B4', arrowstyle='->'), fontsize=10, color='#4682B4')

# Show the plot
plt.tight_layout()
plt.show()