import matplotlib.pyplot as plt
import numpy as np

hobbies = ['Cook', 'Game', 'Travel', 'Read', 'Exercise']
hours_spent = np.array([15, 12, 10, 7, 5])
happiness_levels = np.array([50, 90, 75, 85, 70])

# Sort the data in descending order based on hours_spent
sorted_indices = np.argsort(hours_spent)[::-1]
hobbies = [hobbies[i] for i in sorted_indices]
hours_spent = hours_spent[sorted_indices]
happiness_levels = happiness_levels[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# Create a bar chart
bars = ax.barh(hobbies, hours_spent, color='lightblue', edgecolor='k')

# Annotate the bars with happiness levels
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