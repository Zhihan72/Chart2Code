import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

energy = [5, 6, 8, 12, 14, 20, 30, 35, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 130, 150, 180, 200, 220, 250, 280, 300,
          350, 400, 450, 480, 510]

transport = [3, 5, 7, 10, 12, 14, 16, 18, 22, 25, 27, 30, 35, 40, 45, 47, 52, 57, 60, 65, 70, 77, 85, 95, 105, 120, 132,
             140, 155, 170, 185]

industry = [4, 6, 8, 11, 12, 18, 25, 30, 34, 36, 40, 43, 47, 50, 54, 60, 67, 75, 82, 90, 100, 110, 120, 135, 150, 165,
            180, 200, 218, 230, 245]

data = np.vstack([energy, transport, industry])

colors = ['#66b3ff', '#ffa07a', '#90ee90']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, labels=['Energy', 'Transport', 'Industry'], colors=colors, alpha=0.7)

ax.set_title('Carbon Emissions Reduction (1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Reduction (M Tons)', fontsize=12)

ax.grid(linestyle='-.', color='gray')

ax.legend(loc='lower right', title='Sectors', fontsize=10, edgecolor='black')

ax.annotate('Industry Efficiency', xy=(2005, 150), xytext=(1992, 250),
            arrowprops=dict(facecolor='gray', arrowstyle='|-|'),
            fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

ax.annotate('Renewable Energy', xy=(2015, 550), xytext=(2002, 700),
            arrowprops=dict(facecolor='gray', arrowstyle='-[', linestyle="--"),
            fontsize=10, bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()