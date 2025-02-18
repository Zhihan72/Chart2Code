import matplotlib.pyplot as plt
import numpy as np

software_dept = [50, 55, 60, 62, 58, 65, 70, 72, 68, 74, 76, 80, 85]
hardware_dept = [30, 35, 40, 42, 38, 45, 50, 52, 48, 54, 56, 60, 65]
marketing_dept = [20, 25, 30, 32, 28, 35, 40, 42, 38, 44, 46, 50, 55]
research_dept = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]

coffee_data = [software_dept, hardware_dept, marketing_dept, research_dept]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(coffee_data, patch_artist=True, vert=False, notch=False,
                boxprops=dict(color='black'),
                medianprops=dict(color='darkred'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', color='black', alpha=0.5, markersize=8))

colors = ['#FF9999', '#66B2FF', '#FFD700', '#FFB6C1']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for i, data in enumerate(coffee_data, start=1):
    y = np.array(data)
    x = np.linspace(i - 0.2, i + 0.2, len(y))
    ax.scatter(y, x, alpha=0.6, edgecolor='w', s=50)

ax.set_ylabel('Divisions', fontsize=14)
ax.set_xlabel('Daily Consumption (Liters)', fontsize=14)
ax.set_yticks(np.arange(1, len(coffee_data) + 1))
ax.set_yticklabels(['Alpha', 'Beta', 'Gamma', 'Delta'], fontsize=12)

plt.title("Weekly Beverage Intake", fontsize=16)
plt.tight_layout()
plt.show()