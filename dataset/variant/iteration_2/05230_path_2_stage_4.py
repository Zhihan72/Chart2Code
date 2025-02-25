import matplotlib.pyplot as plt
import numpy as np

langs = ['Py', 'JS', 'Java', 'C++']
popularity = [30, 25, 20, 15]

years = np.array([2023, 2024, 2025, 2026, 2027])
proj_jobs_growth = {
    'Py': [150, 155, 160, 165, 170],
    'JS': [130, 135, 140, 145, 150],
    'Java': [120, 122, 124, 126, 128],
    'C++': [100, 102, 104, 106, 108]
}

colors = ['#F0DB4F', '#00599C', '#3776AB', '#B07219']
line_styles = ['-', '--', '-.', ':']

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(langs, popularity, color=colors, edgecolor='grey', height=0.6)

for bar, percentage in zip(bars, popularity):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{percentage}%', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

ax2 = ax1.twinx()

for idx, (language, growth) in enumerate(proj_jobs_growth.items()):
    ax2.plot(growth, years, label=f'{language} Growth', color=colors[idx], linestyle=line_styles[idx], marker='o')

ax1.set_title("Lang Pop & Job Growth", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Popularity (%)", fontsize=12)
ax1.set_ylabel("Lang", fontsize=12)
ax2.set_ylabel("Yr", fontsize=12)
ax2.set_yticks(years)

ax1.set_xlim(0, 35)
ax2.set_ylim(2022, 2028)

ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

ax1.set_yticks(np.arange(len(langs)))
ax1.set_yticklabels(langs, fontsize=12, fontweight='bold')

fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85), fontsize=10)

plt.tight_layout()
plt.show()