import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

age_18_25 = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
age_26_35 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
age_36_50 = np.array([40, 42, 45, 47, 50, 53, 56, 59, 62, 65, 70])
age_51_65 = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])
age_65_above = np.array([10, 12, 14, 16, 18, 20, 23, 25, 27, 30, 32])

consumption_data = np.vstack([age_18_25, age_26_35, age_36_50, age_51_65, age_65_above])

plt.figure(figsize=(14, 9))

colors = ['#c2c2f0', '#ffcc99', '#99ff99', '#ff9999', '#66b3ff']

plt.stackplot(years, consumption_data, labels=['18-25', '26-35', '36-50', '51-65', '65+'], colors=colors, alpha=0.9, linestyle='-.')

plt.title('Coffee Consumption Trends for Age Groups (2010-2020)', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=13)
plt.ylabel('Consumption (Thousand Cups/Day)', fontsize=13)

plt.legend(loc='upper right', bbox_to_anchor=(1, 0.5), title='Age Groups', fontsize=11, frameon=True)

plt.grid(False)

plt.annotate('Increase Detected', xy=(2017, 85), xytext=(2012, 110),
             arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.2),
             fontsize=12, color='purple')

for i in range(len(years)):
    if i == len(years) - 1:
        plt.text(years[i], consumption_data[1, i] + 3, f'{consumption_data[1, i]}', color=colors[3], fontsize=10, fontweight='bold')
        plt.text(years[i], consumption_data[0, i] + consumption_data[1, i] + 3, f'{consumption_data[0, i]}', color=colors[4], fontsize=10, fontweight='bold')

plt.tight_layout()

plt.show()