import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

energy = [5, 6, 8, 12, 14, 20, 30, 35, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 130, 150, 180, 200, 220, 250, 280, 300, 
          350, 400, 450, 480, 510]
transport = [3, 5, 7, 10, 12, 14, 16, 18, 22, 25, 27, 30, 35, 40, 45, 47, 52, 57, 60, 65, 70, 77, 85, 95, 105, 120, 132, 
             140, 155, 170, 185]
industry = [4, 6, 8, 11, 12, 18, 25, 30, 34, 36, 40, 43, 47, 50, 54, 60, 67, 75, 82, 90, 100, 110, 120, 135, 150, 165,
            180, 200, 218, 230, 245]
agriculture = [2, 2.5, 3, 4, 5, 6, 7, 8.5, 10, 11.5, 13, 14, 16, 18, 19.5, 21, 23.5, 26, 29, 32, 35, 38, 40, 43, 47, 51,
               54, 58, 61, 65, 68]
technology = [0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 9, 11, 13, 15, 18, 21, 24, 28, 32, 37, 43, 50, 58, 67, 77, 88, 100, 
              113, 127, 142, 158]

data = np.vstack([energy, transport, industry, agriculture, technology])

# Set a single consistent color for all data groups
consistent_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Power', 'Commute', 'Manufacturing', 'Farming', 'Innovation'], 
             colors=[consistent_color] * data.shape[0], alpha=0.8)

ax.set_title('Worldwide CO2 Reduction by Category (1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Reduction Volume (Million Tons)', fontsize=12)

ax.grid(linestyle='--', alpha=0.6)
ax.legend(loc='upper left', title='Categories', fontsize=10)

ax.annotate('Efficiency Boost in Factories', xy=(2005, 150), xytext=(1995, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

ax.annotate('Renewables Takeover', xy=(2015, 550), xytext=(2000, 650),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()