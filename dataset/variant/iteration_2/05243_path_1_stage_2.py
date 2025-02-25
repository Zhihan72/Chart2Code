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
fig, ax1 = plt.subplots(figsize=(8, 8))

# First subplot: Line chart of investments over years
ax1.plot(years, solaria_investment, marker='o', linestyle='-', color='#FF4500', linewidth=2, label='Solaria')
ax1.plot(years, ventura_investment, marker='s', linestyle='--', color='#1E90FF', linewidth=2, label='Ventura')
ax1.plot(years, hydrona_investment, marker='^', linestyle='-.', color='#2E8B57', linewidth=2, label='Hydrona')
ax1.plot(years, geotherma_investment, marker='D', linestyle=':', color='#FFD700', linewidth=2, label='Geotherma')

ax1.set_title('Renewable Energy Investment Growth (2000-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Investment (Billion Dollars)', fontsize=14)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)
ax1.legend(title='Countries', loc='best', fontsize=12)

# Annotating specific points
ax1.annotate('Solaria Boom', xy=(2016, 35), xytext=(2008, 40),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#FF4500')
ax1.annotate('Ventura Surge', xy=(2020, 40), xytext=(2012, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#1E90FF')

# Show the plot
plt.tight_layout()
plt.show()