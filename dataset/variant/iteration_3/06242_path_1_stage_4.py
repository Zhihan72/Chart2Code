import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

age_18_25 = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
age_26_35 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
age_36_50 = np.array([40, 42, 45, 47, 50, 53, 56, 59, 62, 65, 70])
age_51_65 = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])
age_65_above = np.array([10, 12, 14, 16, 18, 20, 23, 25, 27, 30, 32])
age_under_18 = np.array([5, 7, 9, 10, 12, 13, 15, 17, 18, 19, 20])

consumption_data = np.vstack([
    age_under_18, age_18_25, age_26_35, age_36_50, age_51_65, age_65_above
])

plt.figure(figsize=(14, 9))

# New set of colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#f0e68c']

plt.stackplot(years, consumption_data, 
              labels=['<18', '18-25', '26-35', '36-50', '51-65', '65+'], 
              colors=colors, alpha=0.9, linestyle='-.')

plt.title('Coffee Trends by Age', fontsize=18, fontweight='bold')
plt.xlabel('Yr', fontsize=13)
plt.ylabel('Cups/Day (000s)', fontsize=13)

plt.legend(loc='upper right', bbox_to_anchor=(1, 0.5), title='Age', fontsize=11, frameon=True)

plt.grid(False)

plt.annotate('Increase', xy=(2017, 85), xytext=(2012, 110),
             arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.2),
             fontsize=12, color='purple')

for i in range(len(years)):
    if i == len(years) - 1:
        plt.text(years[i], consumption_data[2, i] + 3, f'{consumption_data[2, i]}', color=colors[4], fontsize=10, fontweight='bold')
        plt.text(years[i], consumption_data[1, i] + consumption_data[2, i] + 3, f'{consumption_data[1, i]}', color=colors[5], fontsize=10, fontweight='bold')

plt.tight_layout()

plt.show()