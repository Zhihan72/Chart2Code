import matplotlib.pyplot as plt
import numpy as np

stages = ["Idea", "Prototype", "Alpha", "Beta", "Launch", "Success"]
projects = np.array([500, 300, 200, 100, 50, 30])
single_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', color='gray')
ax.xaxis.grid(False)

ax.set_title('Innovation Funnel', fontsize=14, style='italic', pad=25)

plt.tight_layout()

categories = ['Soft', 'Hard', 'Service', 'Hybrid']
category_counts = [250, 150, 75, 25]

fig2, ax2 = plt.subplots(figsize=(8, 8))

ax2.pie(category_counts, labels=[None]*len(categories), colors=[single_color]*len(categories), autopct='%1.1f%%',
        startangle=100, wedgeprops={'edgecolor': 'navy', 'linestyle': '-', 'width': 0.4})

ax2.set_title('Idea Categories', fontsize=14, style='italic', pad=15)

ax2.legend(categories, loc='upper left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()