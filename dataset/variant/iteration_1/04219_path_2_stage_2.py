import matplotlib.pyplot as plt
import numpy as np

stages = ["Idea", "Prototype", "Alpha", "Beta", "Launch", "Success"]
projects = np.array([500, 300, 200, 100, 50, 30])
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e4']

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

ax.set_title('Innovation Funnel', fontsize=16, weight='bold', pad=20)

plt.tight_layout()

categories = ['Soft', 'Hard', 'Service', 'Hybrid']
category_counts = [250, 150, 75, 25]
pie_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(category_counts, labels=categories, colors=pie_colors, autopct='%1.1f%%',
        startangle=140, wedgeprops={'edgecolor': 'black', 'width': 0.3})

ax2.set_title('Idea Categories', fontsize=16, weight='bold', pad=10)

plt.tight_layout()
plt.show()