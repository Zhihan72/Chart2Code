import matplotlib.pyplot as plt
import numpy as np

# Data with removed groups (December - smallest, June - largest rainfall)
months = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10, 11])
rainfall = np.array([85, 78, 92, 110, 134, 102, 75, 65, 45, 40])

# Sort both months and rainfall based on the rainfall values (descending order)
sorted_indices = np.argsort(rainfall)[::-1]
months_sorted = months[sorted_indices]
rainfall_sorted = rainfall[sorted_indices]

# Manually shuffled colors for the remaining months
shuffled_colors = ['lightgreen', 'gold', 'coral', 'skyblue', 
                   'gold', 'lightgreen', 'coral', 'gold', 'coral', 'lightgreen']

fig, ax = plt.subplots(figsize=(14, 8))

bars = ax.bar(months_sorted, rainfall_sorted, color=shuffled_colors, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

ax.set_title("Monthly Rainfall (Sorted)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Rainfall (mm)", fontsize=14)

month_labels_sorted = [f'{months[i]}' for i in sorted_indices]
ax.set_xticks(months_sorted)
ax.set_xticklabels(month_labels_sorted, fontsize=12)

plt.tight_layout()
plt.show()