import matplotlib.pyplot as plt
import numpy as np

# Changing kingdom names and victory numbers manually
kingdoms = ['Zarland', 'Qiran', 'Vorlune', 'Pyrannia']
total_victories = np.array([53, 41, 48, 52])

# Sorting the changed arrays
sorted_indices = np.argsort(total_victories)[::-1]
sorted_kingdoms = [kingdoms[i] for i in sorted_indices]
sorted_victories = total_victories[sorted_indices]

# Colors remain the same, but they can be shuffled if necessary
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
sorted_colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_kingdoms, sorted_victories, color=sorted_colors)

# Randomly altered textual elements
ax.set_xlabel('Nations', fontsize=14)
ax.set_ylabel('Champion Wins', fontsize=14)
ax.set_title('Sorted Wins by Nations', fontsize=16, fontweight='bold')

for i, victory in enumerate(sorted_victories):
    ax.text(i, victory + 0.5, str(victory), ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()