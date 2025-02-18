import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
march_extent = [15.64, 15.61, 15.48, 15.36, 15.25, 14.94, 14.80, 14.71, 14.65, 14.55, 14.35, 14.26, 14.16, 14.10, 14.04, 13.91, 13.83, 13.80, 13.66, 13.54, 13.41]
june_extent = [11.34, 11.29, 11.23, 11.08, 10.94, 10.74, 10.51, 10.33, 10.14, 10.05, 9.91, 9.75, 9.59, 9.41, 9.28, 9.13, 9.00, 8.89, 8.75, 8.65, 8.53]
september_extent = [6.41, 6.37, 6.30, 6.14, 5.97, 5.75, 5.55, 5.36, 5.20, 5.10, 4.92, 4.76, 4.63, 4.50, 4.38, 4.24, 4.12, 4.00, 3.88, 3.76, 3.67]
december_extent = [13.54, 13.52, 13.49, 13.42, 13.30, 13.11, 12.93, 12.82, 12.63, 12.48, 12.30, 12.13, 11.96, 11.81, 11.67, 11.52, 11.38, 11.27, 11.15, 11.03, 10.91]

fig, ax = plt.subplots(figsize=(14, 8))

# New colors for the plot
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
months = ['March', 'June', 'September', 'December']
extents = [march_extent, june_extent, september_extent, december_extent]
markers = ['o', 's', 'D', '^']

for extent, month, color, marker in zip(extents, months, colors, markers):
    ax.plot(years, extent, label=month, color=color, marker=marker, linewidth=2)

    for (x, y) in zip(years, extent):
        ax.annotate(f'{y:.2f}M km²', xy=(x, y), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontsize=8, color=color)

ax.set_title('Arctic Sea Ice Extent:\nImpact of Climate Change Over Two Decades (2000-2020)', 
              fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sea Ice Extent (Million km²)', fontsize=12)

ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.axhline(y=10.0, color='r', linestyle='-', linewidth=1.5, alpha=0.7)
ax.text(2000.5, 10.2, 'Sensitive Threshold: 10M km²', color='r', fontsize=10)

ax.legend(title='Months', title_fontsize='13', loc='upper right', frameon=False)

plt.tight_layout()
plt.show()