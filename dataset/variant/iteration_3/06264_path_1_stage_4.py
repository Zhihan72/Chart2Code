import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2026)

fruits_consumption = [105, 22, 90, 26, 100, 44, 35, 76, 40, 64, 110, 52, 20, 60, 24, 95, 48, 32, 72, 85, 80, 38, 56, 115, 29, 68]
vegetables_consumption = [116, 17, 88, 98, 73, 78, 32, 42, 25, 22, 46, 63, 83, 68, 104, 54, 58, 93, 50, 122, 110, 20, 35, 38, 15, 28]
meats_consumption = [30, 39, 25, 102, 47, 51, 138, 35, 55, 28, 65, 126, 144, 108, 75, 114, 43, 96, 120, 32, 85, 60, 132, 70, 80, 90]
dairy_consumption = [11.8, 30.2, 25.2, 24.2, 26.2, 18.2, 15.3, 33.2, 21.2, 22.2, 28.2, 12.6, 19.2, 20.2, 31.2, 16.2, 17.2, 32.2, 29.2, 13.5, 14.4, 10.5, 11, 10, 23.2, 27.2]

data = np.vstack([fruits_consumption, vegetables_consumption, meats_consumption, dairy_consumption])
single_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, colors=[single_color]*4, alpha=0.8)

ax.set_title('Shifting Patterns in Diet Habits\nExplore the Consumption Spectrum (2000-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline (Years)', fontsize=12)
ax.set_ylabel('Usage in Thousands', fontsize=12)

ax.annotate('Sharp increase in Protein intake', xy=(2015, 70), xytext=(2010, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='red')
ax.annotate('Steady uptick in Herb preference', xy=(2018, 82), xytext=(2015, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()