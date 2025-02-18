import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
gas_vehicles = np.array([50, 48, 45, 40, 35, 30, 25, 20, 15, 10, 5])
electric_vehicles = np.array([1, 2, 4, 6, 10, 15, 25, 30, 40, 50, 65])
hybrid_vehicles = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 38])
public_transport = np.array([30, 31, 32, 33, 34, 33, 34, 35, 36, 37, 38])

vehicle_data = np.vstack([gas_vehicles, electric_vehicles, hybrid_vehicles, public_transport])
colors = ['#ff9999', '#66b3ff', '#99ff99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, vehicle_data, colors=colors, alpha=0.8)

ax.set_title('Vehicle Trends in Automotiville (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Thousands', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 81, 10))

ax.annotate('EVs rise', xy=(2015, 20), xytext=(2016, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=10, color='blue')

ax.annotate('Gas declines', xy=(2015, 35), xytext=(2013, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-.2'), fontsize=10, color='red')

plt.tight_layout()
plt.show()