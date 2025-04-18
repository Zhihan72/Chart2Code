import matplotlib.pyplot as plt
import numpy as np

# Define years from 1990 to 2020
years = np.arange(1990, 2021)

# Global Carbon Emissions Reductions (in million tons) from different sectors
energy = [5, 6, 8, 12, 14, 20, 30, 35, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 130, 150, 180, 200, 220, 250, 280, 300,
          350, 400, 450, 480, 510]

transport = [3, 5, 7, 10, 12, 14, 16, 18, 22, 25, 27, 30, 35, 40, 45, 47, 52, 57, 60, 65, 70, 77, 85, 95, 105, 120, 132,
             140, 155, 170, 185]

industry = [4, 6, 8, 11, 12, 18, 25, 30, 34, 36, 40, 43, 47, 50, 54, 60, 67, 75, 82, 90, 100, 110, 120, 135, 150, 165,
            180, 200, 218, 230, 245]

agriculture = [2, 2.5, 3, 4, 5, 6, 7, 8.5, 10, 11.5, 13, 14, 16, 18, 19.5, 21, 23.5, 26, 29, 32, 35, 38, 40, 43, 47, 51,
               54, 58, 61, 65, 68]

data = np.vstack([energy, transport, industry, agriculture])

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Energy', 'Transport', 'Industry', 'Agri'], colors=colors, alpha=0.8)

ax.set_title('Carbon Emissions Reduction (1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Reduction (M Tons)', fontsize=12)

ax.grid(linestyle='--', alpha=0.6)
ax.legend(loc='upper left', title='Sectors', fontsize=10)

ax.annotate('Industry Efficiency', xy=(2005, 150), xytext=(1995, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

ax.annotate('Renewable Energy', xy=(2015, 550), xytext=(2000, 650),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()