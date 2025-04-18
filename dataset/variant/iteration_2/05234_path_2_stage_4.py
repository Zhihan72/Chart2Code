import matplotlib.pyplot as plt
import numpy as np

hobbies = ['Cook', 'Game', 'Travel', 'Read', 'Exercise']
# Manually shuffled hours_spent and happiness_levels while preserving dimensional structure
hours_spent = np.array([7, 10, 12, 5, 15])
happiness_levels = np.array([85, 75, 90, 70, 50])

# Sort the data in descending order based on hours_spent
sorted_indices = np.argsort(hours_spent)[::-1]
hobbies = [hobbies[i] for i in sorted_indices]
hours_spent = hours_spent[sorted_indices]
happiness_levels = happiness_levels[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(hobbies, hours_spent, color='lightblue', edgecolor='k')

for bar, happiness, hobby in zip(bars, happiness_levels, hobbies):
    ax.annotate(f'Happiness: {happiness}', 
                (bar.get_width(), bar.get_y() + bar.get_height() / 2), 
                xytext=(5, 0), textcoords='offset points', 
                ha='left', va='center', fontsize=12, fontweight='bold')

ax.set_title('Exploring Hobby Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours per Week Engaged', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()