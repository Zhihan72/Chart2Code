import matplotlib.pyplot as plt
import numpy as np

# Fictional research data about the concentration of different elements in Earth's core samples
elements = ['Iron', 'Nickel', 'Oxygen', 'Sulfur', 'Silicon', 'Magnesium']
core_sample_A = [75, 5, 10, 3, 5, 2]
core_sample_B = [80, 4, 11, 2, 4, 3]
core_sample_C = [78, 6, 9, 4, 3, 2]
core_sample_D = [76, 5, 8, 3, 7, 1]
core_sample_E = [77, 6, 10, 4, 2, 1]

data = [core_sample_A, core_sample_B, core_sample_C, core_sample_D, core_sample_E]

# Additional data for average concentration percentages
average_concentration = np.mean(data, axis=0)

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Box Plot on the left
bp = ax1.boxplot(data, patch_artist=True, notch=False, widths=0.5,
                 boxprops=dict(facecolor='#ffcccb', color='black'),
                 whiskerprops=dict(color='black', linestyle='--'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='blue', linewidth=2),
                 flierprops=dict(marker='o', color='black', alpha=0.5))

colors = ['#FF9999', '#FFB6C1', '#FFA07A', '#FF6347', '#FF4500']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

ax1.set_title("Elemental Concentration Analysis in Core Samples:\nInsights into Earth's Inner Composition",
              fontsize=14, fontweight='bold')
ax1.set_ylabel("Concentration (%)", fontsize=12)
ax1.set_xlabel("Core Samples", fontsize=12)
ax1.set_xticklabels(["Sample A", "Sample B", "Sample C", "Sample D", "Sample E"],
                    fontsize=10, rotation=15)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Bar Plot on the right
x = np.arange(len(elements))  # the label locations
width = 0.4  # the width of the bars

# Plot the average concentration of each element
ax2.bar(x, average_concentration, width, label='Average Concentration', color='#4682B4')

ax2.set_title("Average Elemental Concentration Across Core Samples", fontsize=14, fontweight='bold')
ax2.set_ylabel("Average Concentration (%)", fontsize=12)
ax2.set_xlabel("Elements", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(elements, fontsize=10, rotation=15)
ax2.legend(title="Elements", fontsize=9, title_fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout automatically
plt.tight_layout()

# Show the plots
plt.show()