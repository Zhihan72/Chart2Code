import matplotlib.pyplot as plt
import numpy as np

preferences = [
    [30, 25, 20, 15, 10],
    [10, 10, 40, 30, 10],
    [15, 20, 30, 20, 15],
    [20, 30, 20, 10, 20],
    [25, 15, 25, 20, 15],
    [20, 25, 25, 15, 15],
]
colors = ['#FFD700', '#32CD32', '#FF6347', '#87CEFA', '#D2B48C']

fig, axes = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect="equal"))

for i, ax in enumerate(axes.flat):
    wedges, _, autotexts = ax.pie(
        preferences[i], autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.75,  # Modified distance
        wedgeprops=dict(width=0.4, edgecolor='black'),  # Modified the width and added edge color
        shadow=False  # Removed shadow
    )

    # Randomly alter text properties
    for autotext in autotexts:
        autotext.set_color('black')  # Changed text color to black
        autotext.set_fontsize(12)    # Made text visible with size 12

# Add a border to the entire plot
for spine in fig.gca().spines.values():
    spine.set_edgecolor('#333333')
    spine.set_linewidth(2)

# Add a grid on top of the plots
for ax in axes.flat:
    ax.grid(True, which='both', axis='both', color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.legend(['A', 'B', 'C', 'D', 'E'], loc='upper right', bbox_to_anchor=(1.2, 1), borderaxespad=0)
plt.show()