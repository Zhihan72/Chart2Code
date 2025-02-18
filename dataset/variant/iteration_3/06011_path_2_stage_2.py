import matplotlib.pyplot as plt
import numpy as np

regions = ['Region B', 'Region D', 'Region E', 'Region A', 'Region C']
apples = [850, 950, 1100, 1200, 1250]
oranges = [1200, 950, 1020, 900, 820]
grapes = [950, 1200, 980, 880, 1100]
total_production = np.array(apples) + np.array(oranges) + np.array(grapes)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6

ax.bar(regions, apples, label='Apples', color='#FF6347', width=bar_width, hatch='/')
ax.bar(regions, oranges, bottom=apples, label='Oranges', color='#FFA500', width=bar_width, hatch='\\')
ax.bar(regions, grapes, bottom=np.array(apples) + np.array(oranges), label='Grapes', color='#9370DB', width=bar_width, hatch='x')

ax.set_title("Fruit Production by Region in 2023", fontsize=16, loc='left')
ax.set_xlabel("Regions", fontsize=12)
ax.set_ylabel("Production (kg)", fontsize=12)
ax.set_ylim(0, max(total_production) + 300)

ax.legend(title="Fruit Varieties", loc='upper left', ncol=2)

ax.grid(axis='y', linestyle='-.', alpha=0.5)

for idx, (region, total) in enumerate(zip(regions, total_production)):
    ax.text(idx, total + 50, f"{total} kg", ha='center', va='bottom', fontsize=9, fontweight='regular', rotation=30)

plt.xticks(rotation=20, ha='center')

plt.tight_layout()

plt.show()