import matplotlib.pyplot as plt
import numpy as np

# Energy sources and countries (arbitrary data)
sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind']
countries = ['USA', 'China', 'Germany', 'India']

# Energy production data in TWh for each country and source
energy_data = [
    [1000, 1200, 800, 500, 300, 400],  # USA
    [1500, 2000, 1000, 800, 600, 700],  # China
    [300, 450, 900, 700, 500, 600],     # Germany
    [1400, 1200, 200, 600, 400, 300],   # India
]

average_production = np.mean(energy_data, axis=0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

# Randomly altering stack order and color for diversity
bar_width = 0.65
colors = ['#ff7f0e', '#1f77b4', '#d62728', '#2ca02c', '#8c564b', '#9467bd']
bottoms = np.zeros(len(countries))

# Altering line and marker styles
line_styles = ['-', '--', '-.', ':', '-', '--']

for source_idx, (source, color) in enumerate(zip(sources, colors)):
    source_data = [country_data[source_idx] for country_data in energy_data]
    bars = ax1.bar(countries, source_data, width=bar_width, bottom=bottoms, color=color, edgecolor='grey', label=source)
    bottoms += source_data

for bars in ax1.containers:
    ax1.bar_label(bars, label_type='center', fmt='%.0f TWh', fontsize=9)

ax1.set_ylabel('Energy Production (TWh)', fontsize=12)
ax1.set_title('Energy Production by Source in Different Countries, 2023', fontsize=16, fontweight='bold', pad=20)
ax1.legend(title='Energy Source', loc='upper right', fontsize=10)  # Changed location
ax1.grid(axis='y', linestyle='-.', alpha=0.5)  # Changed grid style

# Global average production bar chart
ax2.bar(sources, average_production, color=colors, edgecolor='grey', width=bar_width)  # Consistent colors
for i, val in enumerate(average_production):
    ax2.text(i, val + 10, f'{val:.1f} TWh', ha='center', va='bottom', fontsize=11)

ax2.set_ylabel('Avg. Global Production (TWh)', fontsize=12)
ax2.set_title('Average Global Energy Production by Source, 2023', fontsize=16, pad=20)
ax2.set_xticklabels(sources, rotation=30, ha='right')  # Changed rotation
ax2.grid(axis='y', linestyle=':', alpha=0.7)  # Different grid style

plt.tight_layout()
plt.show()