import matplotlib.pyplot as plt
import numpy as np

kingdoms = ['Zarland', 'Qiran', 'Vorlune', 'Pyrannia']
total_victories = np.array([53, 41, 48, 52])

sorted_indices = np.argsort(total_victories)[::-1]
sorted_kingdoms = [kingdoms[i] for i in sorted_indices]
sorted_victories = total_victories[sorted_indices]

# Updated colors with a new set
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3']
sorted_colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_kingdoms, sorted_victories, color=sorted_colors)

ax.set_xlabel('Nations', fontsize=14)
ax.set_ylabel('Champion Wins', fontsize=14)
ax.set_title('Sorted Wins by Nations', fontsize=16, fontweight='bold')

for i, victory in enumerate(sorted_victories):
    ax.text(i, victory + 0.5, str(victory), ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()