import matplotlib.pyplot as plt
import numpy as np

body_assembly = [45, 50, 48, 52, 46, 49, 47, 51, 50, 48, 47, 46, 50, 51, 49, 52, 48, 50]
painting = [30, 34, 32, 33, 31, 35, 34, 32, 30, 33, 34, 32, 31, 30, 32, 34, 35, 33]
engine_installation = [60, 65, 63, 64, 66, 62, 61, 67, 62, 63, 65, 66, 64, 61, 65, 67, 63, 66]
interior_assembly = [40, 42, 41, 39, 43, 42, 40, 41, 43, 39, 42, 41, 40, 43, 42, 39, 43, 40]
quality_control = [20, 22, 21, 23, 20, 24, 21, 22, 20, 22, 21, 20, 24, 23, 21, 22, 24, 23]

data = [body_assembly, painting, engine_installation, interior_assembly, quality_control]
stages = ['Assembly', 'Paint', 'Engine', 'Interior', 'QC']

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Shuffle the box plot colors assigned to each data group
axs[0].boxplot(data, vert=False, patch_artist=True, notch=True,
               boxprops=dict(facecolor="lightblue", color="navy"),
               whiskerprops=dict(color="navy"),
               capprops=dict(color="navy"),
               medianprops=dict(color="darkred"),
               flierprops=dict(markerfacecolor='orange', marker='o', alpha=0.5))

axs[0].set_title('Stage Time Variability', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Time (min)')
axs[0].set_yticklabels(stages)
axs[0].grid(linestyle='--', alpha=0.7)

# Shuffle the bar chart colors assigned to each type
average_processing_time = [np.mean(stage) for stage in data]
stage_indices = np.arange(len(stages))

axs[1].bar(stage_indices, average_processing_time, color='lightcoral', edgecolor='darkred')
axs[1].set_xticks(stage_indices)
axs[1].set_xticklabels(stages, rotation=20, ha='right')
axs[1].set_title('Avg Time per Stage', fontsize=14, fontweight='bold')
axs[1].set_ylabel('Avg Time (min)')
axs[1].grid(linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()