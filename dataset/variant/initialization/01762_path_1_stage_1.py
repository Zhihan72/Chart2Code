import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051, 10)
energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Renewables']
coal = [40, 35, 30, 25, 20, 15]
natural_gas = [25, 25, 20, 20, 18, 15]
nuclear = [10, 10, 12, 14, 15, 15]
hydroelectric = [10, 12, 13, 14, 15, 16]
renewables = [5, 8, 15, 20, 32, 39]
data = np.vstack([coal, natural_gas, nuclear, hydroelectric, renewables])
total_energy_consumption = [8000, 8500, 9000, 9500, 10000, 10500]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
fig.suptitle('Energy Evolution and Total Consumption in the 21st Century', fontsize=16, fontweight='bold', y=0.95)

colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax1.stackplot(years, data, colors=colors, alpha=0.8, edgecolor='grey')
ax1.set_title('Share of Energy Sources', fontsize=12, pad=10)
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Percentage of Total Energy (%)', fontsize=10)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 10))

ax2.plot(years, total_energy_consumption, marker='o', color='#17becf', linestyle='-', linewidth=2)
ax2.set_title('Total Energy Consumption', fontsize=12, pad=10)
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Energy Consumption (TWh)', fontsize=10)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(8000, 11001, 500))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()