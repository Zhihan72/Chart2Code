import matplotlib.pyplot as plt
import numpy as np

stages = ["Idea", "Proto", "Alpha", "Beta", "Intro", "Success"]
projects = np.array([500, 300, 200, 100, 50, 30])

fig, ax = plt.subplots(figsize=(10, 8))

# Text labels for each stage without additional styling
for i in range(len(stages)):
    ax.text(0.5, i + 0.5, f"{stages[i]}\n{projects[i]}", 
            ha='center', va='center', fontsize=12, color='black')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')  # Remove axes
plt.tight_layout()

categories = ['Soft', 'Hard', 'Serv', 'Hybrid']
category_counts = [250, 150, 75, 25]

fig2, ax2 = plt.subplots(figsize=(8, 8))

# Donut chart without additional styling
ax2.pie(category_counts, colors=['skyblue']*len(categories), autopct='%1.1f%%',
        startangle=140, wedgeprops={'width': 0.3})

plt.tight_layout()
plt.show()