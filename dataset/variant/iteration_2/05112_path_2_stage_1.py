import matplotlib.pyplot as plt
import numpy as np

# Energy sources and countries (arbitrary data)
sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind']
countries = ['USA', 'China', 'Germany', 'India', 'Brazil']

# Energy production data in TWh for each country and source
energy_data = [
    [1000, 1200, 800, 500, 300, 400],  # USA
    [1500, 2000, 1000, 800, 600, 700],  # China
    [300, 450, 900, 700, 500, 600],     # Germany
    [1400, 1200, 200, 600, 400, 300],   # India
    [200, 300, 100, 900, 800, 700]      # Brazil
]

# Compute deviation from average for diverging effect
average_production = np.mean(energy_data, axis=0)
deviation_data = energy_data - average_production

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

# Plot diverging bar chart for each country
bar_width = 0.7
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bottoms_pos = np.zeros(len(countries))
bottoms_neg = np.zeros(len(countries))

# Plotting diverging bars
for source_idx, (source, color) in enumerate(zip(sources, colors)):
    source_data = deviation_data[:, source_idx]
    pos_data = np.where(source_data >= 0, source_data, 0)
    neg_data = np.where(source_data < 0, source_data, 0)
    
    ax1.bar(countries, pos_data, width=bar_width, bottom=bottoms_pos, color=color, edgecolor='black', label=source)
    ax1.bar(countries, neg_data, width=bar_width, bottom=bottoms_neg, color=color, edgecolor='black')
    
    bottoms_pos += pos_data
    bottoms_neg += neg_data

# Labels and titles
ax1.set_ylabel('Deviation from Avg. Energy Production (TWh)', fontsize=12)
ax1.set_title('Diverging Energy Production by Source in Different Countries, 2023', fontsize=16, fontweight='bold', pad=20)
ax1.legend(title='Energy Source', loc='upper left', fontsize=10)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Average production bar chart
ax2.bar(sources, average_production, color=['#61a4b2'], edgecolor='black', width=bar_width)
ax2.set_ylabel('Avg. Global Production (TWh)', fontsize=12)
ax2.set_title('Average Global Energy Production by Source, 2023', fontsize=16, pad=20)
ax2.set_xticklabels(sources, rotation=45, ha='right')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()