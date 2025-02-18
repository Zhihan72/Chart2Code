import matplotlib.pyplot as plt
import numpy as np

software_dept = [55, 50, 60, 62, 58, 65, 72, 70, 68, 74, 76, 85, 80]
hardware_dept = [30, 35, 40, 42, 48, 45, 38, 52, 54, 60, 56, 65, 50]
hr_dept = [12, 10, 14, 16, 20, 18, 22, 25, 30, 28, 31, 35, 34]
marketing_dept = [20, 25, 32, 30, 28, 44, 38, 35, 40, 46, 50, 42, 55]
research_dept = [65, 60, 70, 80, 75, 90, 85, 95, 100, 105, 110, 120, 115]

coffee_data = [software_dept, hardware_dept, hr_dept, marketing_dept, research_dept]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(coffee_data, patch_artist=True, vert=False, notch=False,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='darkred', linewidth=2),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                flierprops=dict(marker='o', color='black', alpha=0.5, markersize=8))

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for i, data in enumerate(coffee_data, start=1):
    x = np.array(data)
    y = np.random.normal(i, 0.04, size=len(x))
    ax.scatter(x, y, alpha=0.6, edgecolor='w', s=50, label=f'{["Software", "Hardware", "HR", "Marketing", "Research"][i-1]} Points' if i == 1 else "")

ax.set_title('Weekly Coffee Consumption Across Departments\nTechCorp Q3 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Coffee Consumption (Cups)', fontsize=14)
ax.set_ylabel('Departments', fontsize=14)
ax.set_yticks(np.arange(1, len(coffee_data) + 1))
ax.set_yticklabels(['Software', 'Hardware', 'HR', 'Marketing', 'Research'], fontsize=12)

ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

for i, dept in enumerate(coffee_data, start=1):
    mean_val = np.mean(dept)
    ax.axvline(mean_val, ls='--', color=colors[i-1], alpha=0.7, linewidth=1.5, label=f'{["Software", "Hardware", "HR", "Marketing", "Research"][i-1]} Mean' if i == 1 else "")
    ax.text(mean_val + 0.5, i, f'{mean_val:.1f}', verticalalignment='center', color=colors[i-1], fontsize=10)

ax.text(0.97, 0.02, "High coffee consumption in Research shows \n the intense work environment.", 
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))

plt.tight_layout()

ax.legend(loc='lower right', fontsize=9)

plt.show()