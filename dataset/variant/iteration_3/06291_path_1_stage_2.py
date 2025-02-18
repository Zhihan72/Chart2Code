import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
vr_categories = ["Games", "Educational", "Social", "Fitness"]

vr_data = np.array([
    [5, 10, 15, 22, 30, 38, 50, 65, 80, 98, 120],
    [1, 2, 3, 5, 8, 12, 18, 25, 33, 43, 55],
    [3, 5, 7, 10, 15, 20, 27, 35, 45, 58, 72],
    [1, 1.5, 2, 4, 7, 11, 16, 22, 29, 37, 46]
])

fig, ax = plt.subplots(figsize=(14, 8))

consistent_color = '#4682B4'  # A consistent single color

# Plot the stacked area chart with a consistent single color
ax.stackplot(years, vr_data, labels=vr_categories, colors=[consistent_color]*len(vr_categories), alpha=0.8)

ax.set_title('Growth of VR Content Consumption Over Years\n(2015-2025)', fontsize=15, fontweight='light', pad=15)
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Consumption (Million Hours)', fontsize=11)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, ha='center')

ax.legend(title='VR Categories', loc='lower left', fontsize=9, fancybox=True, framealpha=0.5)

ax.grid(color='blue', linestyle='-', linewidth=0.6, axis='both', alpha=0.5)

annotations = {
    2022: 'Fitness rise during pandemic',
    2018: 'Growth in Games',
    2025: 'Educational surge'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, vr_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, vr_data[:, years.tolist().index(year)].sum() + 5),
                arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=8, ha='left')

ax2 = ax.twinx()
total_consumption = vr_data.sum(axis=0)
ax2.plot(years, total_consumption, label='Total Consumption', color='purple', linestyle=':', marker='s', markersize=6, linewidth=1.2)
ax2.fill_between(years, total_consumption, color='purple', alpha=0.07)

ax2.set_ylabel('Total Consumption (Million Hours)', fontsize=11)

plt.tight_layout(rect=[0, 0, 0.87, 1])
plt.show()