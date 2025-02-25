import matplotlib.pyplot as plt
import numpy as np

# Energy sources and countries (arbitrary data)
sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind']
countries = ['USA', 'China', 'Germany', 'India']  # Removed 'Brazil'

# Energy production data in TWh for each country and source (Removed Brazil's data)
energy_data = [
    [1000, 1200, 800, 500, 300, 400],  # USA
    [1500, 2000, 1000, 800, 600, 700],  # China
    [300, 450, 900, 700, 500, 600],     # Germany
    [1400, 1200, 200, 600, 400, 300],   # India
]

# Compute the average energy production for each source globally
average_production = np.mean(energy_data, axis=0)

# Create subplots for different visual aspects
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

# Plotting stacked bar for total energy production of each country
bar_width = 0.7
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bottoms = np.zeros(len(countries))

# Plot stacked bars
for source_idx, (source, color) in enumerate(zip(sources, colors)):
    source_data = [country_data[source_idx] for country_data in energy_data]
    bars = ax1.bar(countries, source_data, width=bar_width, bottom=bottoms, color=color, edgecolor='black', label=source)
    bottoms += source_data

# Annotate each source segment with the production value
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='center', fmt='%.0f TWh', fontsize=9)

# Setting labels, title, and legend
ax1.set_ylabel('Energy Production (TWh)', fontsize=12)
ax1.set_title('Energy Production by Source in Different Countries, 2023', fontsize=16, fontweight='bold', pad=20)
ax1.legend(title='Energy Source', loc='upper left', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Plot the global average production as bar chart
ax2.bar(sources, average_production, color=['#61a4b2'], edgecolor='black', width=bar_width)
for i, val in enumerate(average_production):
    ax2.text(i, val + 10, f'{val:.1f} TWh', ha='center', va='bottom', fontsize=11)

# Setting labels and title
ax2.set_ylabel('Avg. Global Production (TWh)', fontsize=12)
ax2.set_title('Average Global Energy Production by Source, 2023', fontsize=16, pad=20)
ax2.set_xticklabels(sources, rotation=45, ha='right')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()