import matplotlib.pyplot as plt
import numpy as np

categories = ['Str', 'Agi', 'Int', 'Cha', 'Res']
num_vars = len(categories)

arthur = [8, 6, 7, 9, 8]
morgana = [7, 8, 9, 6, 7]

average_abilities = [
    np.mean([arthur[i], morgana[i]]) 
    for i in range(num_vars)
]

fig, ax = plt.subplots(figsize=(8, 8))

ax.bar(categories, average_abilities, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.75)
ax.set_ylim(0, 10)
ax.set_title('Adventurers', fontsize=16, style='italic')
ax.set_ylabel('Score', fontsize=12, style='italic')
ax.set_xlabel('Abils', fontsize=12, style='italic')

markers = ['o', '^', 's', 'd', 'v']
for i, score in enumerate(average_abilities):
    ax.plot(i, score, marker=markers[i], markersize=10, color='black')

ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray', axis='y', alpha=0.7)

ax.spines['top'].set_color('none')
ax.spines['right'].set_linestyle('--')
ax.spines['bottom'].set_linewidth(2.0)
ax.spines['left'].set_color('gray')

plt.tight_layout()

plt.show()