import matplotlib.pyplot as plt
import numpy as np

tribes = ['Elves', 'Dwarves', 'Orcs', 'Humans', 'Halflings', 'Goblins', 'Gnomes', 'Trolls', 'Fairies']
average_years_education = np.array([80, 50, 15, 12, 20, 6, 60, 10, 70])

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(tribes, average_years_education, color='skyblue', edgecolor='black', alpha=0.8)

ax.set_title('Education by Tribe', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Avg. Years', fontsize=13)
ax.set_ylabel('Tribes', fontsize=13)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.grid(False)
plt.tight_layout()
plt.show()