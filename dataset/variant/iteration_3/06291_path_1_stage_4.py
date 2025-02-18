import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
vr_categories = ["Games", "Edu", "Social", "Fit"]

vr_data = np.array([
    [22, 38, 30, 98, 15, 50, 5, 120, 65, 10, 80],  # Games
    [1, 12, 3, 5, 43, 18, 33, 2, 25, 55, 8],        # Edu
    [10, 45, 20, 3, 72, 15, 27, 5, 58, 35, 7],      # Social
    [11, 29, 7, 4, 37, 22, 46, 16, 1.5, 2, 1]       # Fit
])

fig, ax = plt.subplots(figsize=(14, 8))

consistent_color = '#4682B4'

ax.stackplot(years, vr_data, labels=vr_categories, colors=[consistent_color]*len(vr_categories), alpha=0.8)

ax.set_title('VR Content Growth\n(2015-25)', fontsize=15, fontweight='light', pad=15)
ax.set_xlabel('Yr', fontsize=11)
ax.set_ylabel('Hours (M)', fontsize=11)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, ha='center')

ax.legend(title='VR Types', loc='lower left', fontsize=9, fancybox=True, framealpha=0.5)

ax.grid(color='blue', linestyle='-', linewidth=0.6, axis='both', alpha=0.5)

annotations = {
    2022: 'Fit rise',
    2018: 'Games growth',
    2025: 'Edu surge'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, vr_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, vr_data[:, years.tolist().index(year)].sum() + 5),
                arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=8, ha='left')

ax2 = ax.twinx()
total_consumption = vr_data.sum(axis=0)
ax2.plot(years, total_consumption, label='Total', color='purple', linestyle=':', marker='s', markersize=6, linewidth=1.2)
ax2.fill_between(years, total_consumption, color='purple', alpha=0.07)

ax2.set_ylabel('Total Hrs (M)', fontsize=11)

plt.tight_layout(rect=[0, 0, 0.87, 1])
plt.show()