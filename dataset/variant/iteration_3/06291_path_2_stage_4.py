import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
vr_data = np.array([
    [5, 10, 15, 22, 30, 38, 50, 65, 80, 98, 120],
    [1, 2, 3, 5, 8, 12, 18, 25, 33, 43, 55],
    [3, 5, 7, 10, 15, 20, 27, 35, 45, 58, 72],
    [1, 1.5, 2, 4, 7, 11, 16, 22, 29, 37, 46],
    [2, 3, 5, 7, 10, 15, 20, 30, 40, 55, 70]
])

fig, ax = plt.subplots(figsize=(14, 8))
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#F7FF33', '#FF33A1']

ax.stackplot(years, vr_data, colors=new_colors, alpha=0.85)

ax.set_title('VR Content Consumption (2015-25)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Consumption (M Hours)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

annotations = {
    2022: 'Growth in Fitness',
    2018: 'Growth in Games',
    2025: 'Edu content rise'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, vr_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, vr_data[:, years.tolist().index(year)].sum() + 7),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

ax2 = ax.twinx()
total_consumption = vr_data.sum(axis=0)
ax2.plot(years, total_consumption, color='black', linestyle='-.', marker='o', linewidth=1.5)
ax2.fill_between(years, total_consumption, color='black', alpha=0.1)
ax2.set_ylabel('Total (M Hours)', fontsize=12)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()