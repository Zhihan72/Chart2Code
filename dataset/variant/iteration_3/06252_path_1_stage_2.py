import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

gas = np.array([50, 48, 45, 40, 35, 30, 25, 20, 15, 10, 5])
electric = np.array([1, 2, 4, 6, 10, 15, 25, 30, 40, 50, 65])
hybrid = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 38])
bikes = np.array([10, 12, 15, 19, 25, 35, 45, 50, 55, 60, 70])
public = np.array([30, 31, 32, 33, 34, 33, 34, 35, 36, 37, 38])

vehicle_data = np.vstack([gas, electric, hybrid, bikes, public])

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, vehicle_data, colors=colors, alpha=0.8)

ax.set_title('Transportation Trends (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Registrations (K)', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 81, 10))

ax.annotate('EVs up', xy=(2015, 20), xytext=(2016, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=10, color='blue')

ax.annotate('Gas down', xy=(2015, 35), xytext=(2013, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-.2'), fontsize=10, color='red')

plt.tight_layout()

plt.show()