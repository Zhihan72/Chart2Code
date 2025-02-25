import matplotlib.pyplot as plt
import numpy as np

# Kingdoms and their total victories
kingdoms = ['Avalon', 'Eldoria', 'Valoria', 'Drakonia']
total_victories = np.array([49, 44, 46, 47])  # Calculated total victories for each kingdom

# Sort kingdoms by total victories in descending order
sorted_indices = np.argsort(total_victories)[::-1]
sorted_kingdoms = [kingdoms[i] for i in sorted_indices]
sorted_victories = total_victories[sorted_indices]

# Colors map for each kingdom
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
sorted_colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_kingdoms, sorted_victories, color=sorted_colors)

# Adding labels and title
ax.set_xlabel('Kingdoms', fontsize=14)
ax.set_ylabel('Total Victories', fontsize=14)
ax.set_title('Total Victories of Kingdoms (Sorted)', fontsize=16, fontweight='bold')

# Annotate bars with the victory numbers
for i, victory in enumerate(sorted_victories):
    ax.text(i, victory + 0.5, str(victory), ha='center', va='bottom', fontsize=10, color='black')

ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()