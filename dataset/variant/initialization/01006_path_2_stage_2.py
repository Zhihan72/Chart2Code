import matplotlib.pyplot as plt
import numpy as np

# Decades remain unchanged
decades = ['1980s', '2000s', '2020s']

# Alter the contents of each data group while maintaining the overall shape
adventure = np.array([20, 15, 25])  # Changed values
cultural = np.array([40, 25, 30])  # Changed values
relaxation = np.array([30, 40, 35])  # Changed values
business = np.array([10, 20, 10])  # Changed values

# Stack data while preserving the structure
data = np.vstack([adventure, cultural, relaxation, business])

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