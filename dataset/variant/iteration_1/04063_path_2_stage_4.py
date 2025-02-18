import matplotlib.pyplot as plt
import numpy as np

elements = ['Iron', 'Nickel', 'Oxygen', 'Sulfur', 'Silicon', 'Magnesium']
core_sample_A = [78, 3, 11, 2, 4, 2]
core_sample_B = [81, 4, 9, 3, 3, 2]
core_sample_C = [79, 5, 8, 4, 3, 3]
core_sample_D = [75, 6, 7, 4, 6, 2]
core_sample_E = [76, 7, 11, 3, 1, 2]

data = [core_sample_A, core_sample_B, core_sample_C, core_sample_D, core_sample_E]
average_concentration = np.mean(data, axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Horizontal Box Plot on the left
bp = ax1.boxplot(data, patch_artist=True, notch=False, widths=0.5,
                 vert=False,
                 boxprops=dict(facecolor='#8FBC8B'),
                 whiskerprops=dict(linestyle='--'),
                 capprops=dict(),
                 medianprops=dict(linewidth=2))

new_colors = ['#87CEEB', '#98FB98', '#FFD700', '#6A5ACD', '#FF69B4']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set(facecolor=color)

ax1.set_xlabel("Concentration (%)", fontsize=12)
ax1.set_ylabel("Core Samples", fontsize=12)
ax1.set_yticklabels(["Sample A", "Sample B", "Sample C", "Sample D", "Sample E"], fontsize=10, rotation=0)

# Bar Plot on the right
x = np.arange(len(elements))
width = 0.4

ax2.bar(x, average_concentration, width, color='#DA70D6')

ax2.set_ylabel("Average Concentration (%)", fontsize=12)
ax2.set_xlabel("Elements", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(elements, fontsize=10, rotation=15)

plt.tight_layout()
plt.show()