import matplotlib.pyplot as plt
import numpy as np

# Stages and project counts
stages = ["Idea", "Proto", "Alpha", "Beta", "Intro", "Success"]
projects = np.array([500, 300, 200, 100, 50, 30])
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e4']

fig, ax = plt.subplots(figsize=(10, 8))

for i in range(len(stages)):
    ax.text(0.5, i + 0.5, f"{stages[i]}\n{projects[i]}", 
            ha='center', va='center', fontsize=12, color='black', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

ax.set_title('Startup Funnel: Idea to Success', fontsize=16, weight='bold', pad=30)

plt.tight_layout()

# Donut chart for idea categories
categories = ['Soft', 'Hard', 'Serv', 'Hybrid']
category_counts = [250, 150, 75, 25]
pie_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

fig2, ax2 = plt.subplots(figsize=(8, 8))

ax2.pie(category_counts, labels=categories, colors=pie_colors, autopct='%1.1f%%',
        startangle=140, wedgeprops={'edgecolor': 'black', 'width': 0.3})

ax2.set_title('Idea Categories', fontsize=16, weight='bold', pad=20)

plt.tight_layout()
plt.show()