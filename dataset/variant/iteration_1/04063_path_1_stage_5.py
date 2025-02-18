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
# Create the bar chart without legend and grid
ax1.bar(x, average_concentration, width, color='#4682B4')
ax1.set_title("Typical Composition of Core Samples", fontsize=14, fontweight='bold')
ax1.set_ylabel("Proportion by Percentage", fontsize=12)
ax1.set_xlabel("Chemical Elements", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(['Fe', 'Ni', 'O', 'S', 'Si', 'Mg'], fontsize=10, rotation=15)

# Create a horizontal boxplot without grid
bp = ax2.boxplot(data, patch_artist=True, vert=False,
                 boxprops=dict(facecolor='#ffcccb', color='black'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='blue', linewidth=2),
                 flierprops=dict(marker='o', color='black', alpha=0.5))

colors = ['#FF4500', '#FF6347', '#FFA07A', '#FFB6C1', '#FF9999']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

ax2.set_title("Core Sample Concentration Distribution:\nExploration of Inner Earth Materials",
              fontsize=14, fontweight='bold')
ax2.set_xlabel("Proportion (%)", fontsize=12)
ax2.set_ylabel("Sample Observations", fontsize=12)
ax2.set_yticklabels(["Obs A", "Obs B", "Obs C", "Obs D", "Obs E"],
                    fontsize=10)

plt.tight_layout()
plt.show()