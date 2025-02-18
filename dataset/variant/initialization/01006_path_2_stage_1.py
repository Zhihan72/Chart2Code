import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '2000s', '2020s']
adventure = np.array([10, 20, 30])
cultural = np.array([30, 30, 25])
relaxation = np.array([40, 35, 40])
business = np.array([20, 15, 5])

data = np.vstack([adventure, cultural, relaxation, business])

# Using a single color consistently across all data groups
single_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, data, labels=['Adventure Travel', 'Cultural Travel', 'Relaxation Travel', 'Business Travel'], colors=[single_color]*4, alpha=0.8)

ax.set_title('Evolution of Travel Preferences\nAcross Decades', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14, weight='bold', labelpad=10)
ax.set_ylabel('Percentage Share of Travel Type', fontsize=14, weight='bold', labelpad=10)

ax.legend(loc='upper left', fontsize=12, title='Travel Categories', title_fontsize='13', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{y}%' for y in np.arange(0, 101, 10)], fontsize=12)
ax.set_xticks(decades)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()