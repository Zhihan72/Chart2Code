import matplotlib.pyplot as plt
import numpy as np

elements = ['Iron', 'Nickel', 'Oxygen', 'Sulfur', 'Silicon', 'Magnesium']
core_sample_A = [75, 5, 10, 3, 5, 2]
core_sample_B = [80, 4, 11, 2, 4, 3]
core_sample_C = [78, 6, 9, 4, 3, 2]
core_sample_D = [76, 5, 8, 3, 7, 1]
core_sample_E = [77, 6, 10, 4, 2, 1]

data = [core_sample_A, core_sample_B, core_sample_C, core_sample_D, core_sample_E]
average_concentration = np.mean(data, axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

x = np.arange(len(elements))
width = 0.4
ax1.bar(x, average_concentration, width, label='Average Concentration', color='#4682B4')
ax1.set_title("Average Elemental Concentration Across Core Samples", fontsize=14, fontweight='bold')
ax1.set_ylabel("Average Concentration (%)", fontsize=12)
ax1.set_xlabel("Elements", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(elements, fontsize=10, rotation=15)
ax1.legend(title="Elements", fontsize=9, title_fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

bp = ax2.boxplot(data, patch_artist=True, notch=False, widths=0.5,
                 boxprops=dict(facecolor='#ffcccb', color='black'),
                 whiskerprops=dict(color='black', linestyle='--'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='blue', linewidth=2),
                 flierprops=dict(marker='o', color='black', alpha=0.5))

# Shuffled colors manually
colors = ['#FF4500', '#FF6347', '#FFA07A', '#FFB6C1', '#FF9999']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

ax2.set_title("Elemental Concentration Analysis in Core Samples:\nInsights into Earth's Inner Composition",
              fontsize=14, fontweight='bold')
ax2.set_ylabel("Concentration (%)", fontsize=12)
ax2.set_xlabel("Core Samples", fontsize=12)
ax2.set_xticklabels(["Sample A", "Sample B", "Sample C", "Sample D", "Sample E"],
                    fontsize=10, rotation=15)
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()