import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051, 10)
energy_sources = ['Renewables', 'Nuclear', 'Natural Gas', 'Coal', 'Hydroelectric']  # Shuffled
coal = [40, 35, 30, 25, 20, 15]
natural_gas = [25, 25, 20, 20, 18, 15]
nuclear = [10, 10, 12, 14, 15, 15]
hydroelectric = [10, 12, 13, 14, 15, 16]
renewables = [5, 8, 15, 20, 32, 39]
data = np.vstack([renewables, nuclear, natural_gas, coal, hydroelectric])  # Reordered to match shuffled labels

fig, ax1 = plt.subplots(figsize=(7, 7))
fig.suptitle('21st Century Energy Changes', fontsize=16, fontweight='bold', y=0.95)  # Altered title

colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax1.stackplot(years, data, colors=colors, alpha=0.8, edgecolor='grey')
ax1.set_title('Energy Source Distribution', fontsize=12, pad=10)  # Altered subtitle
ax1.set_xlabel('Time Period', fontsize=10)  # Altered x-axis label
ax1.set_ylabel('Energy Share (%)', fontsize=10)  # Altered y-axis label
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 10))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()