import matplotlib.pyplot as plt
import numpy as np

sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind']
countries = ['USA', 'China', 'Germany', 'India']

energy_data = [
    [1000, 1200, 800, 500, 300, 400],  # USA
    [1500, 2000, 1000, 800, 600, 700],  # China
    [300, 450, 900, 700, 500, 600],     # Germany
    [1400, 1200, 200, 600, 400, 300],   # India
]

average_production = np.mean(energy_data, axis=0)

fig, (ax2, ax1) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 3]})

# Shuffled colors
colors = ['#9467bd', '#8c564b', '#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']

for idx, (country, data) in enumerate(zip(countries, energy_data)):
    deviation = np.array(data) - average_production
    positive = np.where(deviation > 0, deviation, 0)
    negative = np.where(deviation < 0, deviation, 0)
    
    ax1.barh(sources, positive, left=average_production, color=colors, edgecolor='grey', label=f'{country} Increase' if idx == 0 else None)
    ax1.barh(sources, negative, left=average_production, color=colors, edgecolor='grey', label=f'{country} Decrease' if idx == 0 else None)

ax1.set_xlabel('Deviation from Average Production (TWh)', fontsize=12)
ax1.set_title('Diverging Energy Production by Source in Different Countries, 2023', fontsize=16, fontweight='bold', pad=20)
ax1.legend(title='Energy Production Change', loc='upper right', fontsize=10)
ax1.grid(axis='x', linestyle='-.', alpha=0.5)
ax1.set_yticklabels(sources, rotation=30, ha='right')

ax2.barh(sources, average_production, color=colors, edgecolor='grey')
for i, val in enumerate(average_production):
    ax2.text(val + 50, i, f'{val:.1f} TWh', va='center', fontsize=11)

ax2.set_xlabel('Avg. Global Production (TWh)', fontsize=12)
ax2.set_title('Average Global Energy Production by Source, 2023', fontsize=16, pad=20)
ax2.grid(axis='x', linestyle=':', alpha=0.7)
ax2.set_yticklabels(sources, rotation=30, ha='right')

plt.tight_layout()
plt.show()