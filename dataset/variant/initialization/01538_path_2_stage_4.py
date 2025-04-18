import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

coal = [200, 195, 190, 185, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55]
natural_gas = [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240]
nuclear = [50, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
solar = [5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
wind = [10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100, 120, 140, 160, 180, 200, 220]
hydro = [30, 32, 35, 40, 45, 47, 50, 55, 60, 62, 65, 70, 80, 85, 90, 95, 100, 110, 120, 130, 140]

plt.figure(figsize=(12, 8))

# Changing colors, styles, and including legends
plt.stackplot(years, coal, natural_gas, nuclear, solar, wind, hydro, 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], 
              alpha=0.8, labels=['Coal', 'Natural Gas', 'Nuclear', 'Solar', 'Wind', 'Hydro'])

plt.grid(linestyle='-.', color='grey', alpha=0.6)  # Change grid style and color

plt.legend(loc='upper left')  # Add legend to differentiate energy sources

# Adding border with specific style
plt.gca().spines['top'].set_linestyle(':')
plt.gca().spines['right'].set_linestyle('--')
plt.gca().spines['top'].set_visible(True)  # Show the top border
plt.gca().spines['right'].set_visible(True)  # Show the right border

plt.tight_layout()
plt.show()