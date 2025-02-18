import matplotlib.pyplot as plt
import numpy as np

# Updated stages and project counts
stages = ["Idea", "Proto", "Alpha", "Beta", "Intro", "Success", "Expansion", "Evaluation"]
projects = np.array([500, 300, 200, 100, 50, 30, 20, 10])

fig, ax = plt.subplots(figsize=(10, 8))

# Text labels for each stage
for i in range(len(stages)):
    ax.text(0.5, i + 0.5, f"{stages[i]}\n{projects[i]}", 
            ha='center', va='center', fontsize=12, color='black')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')
plt.tight_layout()

# Updated categories and counts
categories = ['Soft', 'Hard', 'Serv', 'Hybrid', 'IT', 'Biotech']
category_counts = [250, 150, 75, 25, 60, 40]

fig2, ax2 = plt.subplots(figsize=(8, 8))

# Donut chart
ax2.pie(category_counts, colors=['skyblue', 'salmon', 'mediumseagreen', 'gold', 'purple', 'orange'], 
        autopct='%1.1f%%', startangle=140, wedgeprops={'width': 0.3})

plt.tight_layout()
plt.show()