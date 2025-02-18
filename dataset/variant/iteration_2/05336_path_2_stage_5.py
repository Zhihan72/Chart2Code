import matplotlib.pyplot as plt
import numpy as np

regions = ['Americas', 'Europe', 'Asia', 'Africa', 'Oceania', 'Antarctica', 'Atlantis']
internet_users_2020 = [500, 400, 1000, 200, 50, 5, 15]

sorted_indices = np.argsort(internet_users_2020)[::-1]
sorted_regions = [regions[i] for i in sorted_indices]
sorted_internet_users = [internet_users_2020[i] for i in sorted_indices]

colors = ['#48cae4', '#caf0f8', '#0077b6', '#90e0ef', '#00b4d8', '#ffb703', '#fb8500']

fig, ax = plt.subplots(figsize=(10, 6))
bar_positions = np.arange(len(sorted_regions))

bars = ax.bar(bar_positions, sorted_internet_users, color=[colors[i] for i in sorted_indices], width=0.5)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}M',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Region', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_regions, fontsize=12)
ax.set_ylabel('Digital Population (in millions, 2020)', fontsize=12)
ax.set_title('Digital Population by Region in 2020', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()