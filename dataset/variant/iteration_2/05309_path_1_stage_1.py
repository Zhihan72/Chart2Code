import matplotlib.pyplot as plt
import numpy as np

# Data for processing times (in minutes) by stage
body_assembly = [45, 50, 48, 52, 46, 49, 47, 51, 50, 48, 47, 46, 50, 51, 49, 52, 48, 50]
painting = [30, 34, 32, 33, 31, 35, 34, 32, 30, 33, 34, 32, 31, 30, 32, 34, 35, 33]
engine_installation = [60, 65, 63, 64, 66, 62, 61, 67, 62, 63, 65, 66, 64, 61, 65, 67, 63, 66]
interior_assembly = [40, 42, 41, 39, 43, 42, 40, 41, 43, 39, 42, 41, 40, 43, 42, 39, 43, 40]
quality_control = [20, 22, 21, 23, 20, 24, 21, 22, 20, 22, 21, 20, 24, 23, 21, 22, 24, 23]

data = [body_assembly, painting, engine_installation, interior_assembly, quality_control]
stages = ['Body Assembly', 'Painting', 'Engine Installation', 'Interior Assembly', 'Quality Control']

# Create a figure with 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Box plot of processing times for each stage with shuffled colors
axs[0].boxplot(data, vert=True, patch_artist=True, notch=True,
               boxprops=dict(facecolor="lightsalmon", color="darkgreen"),  # Shuffled color
               whiskerprops=dict(color="darkorange"),  # Shuffled color
               capprops=dict(color="darkcyan"),  # Shuffled color
               medianprops=dict(color="darkblue"),  # Shuffled color
               flierprops=dict(markerfacecolor='gold', marker='o', alpha=0.5))  # Shuffled color

axs[0].set_title('Variability in Processing Times Across Production Stages', fontsize=14, fontweight='bold')
axs[0].set_ylabel('Processing Time (minutes)')
axs[0].set_xticklabels(stages, rotation=20, ha='right')
axs[0].grid(linestyle='--', alpha=0.7)

# Bar chart of average processing times with shuffled color
average_processing_time = [np.mean(stage) for stage in data]
stage_indices = np.arange(len(stages))

axs[1].bar(stage_indices, average_processing_time, color='peru', edgecolor='navy')  # Shuffled color
axs[1].set_xticks(stage_indices)
axs[1].set_xticklabels(stages, rotation=20, ha='right')
axs[1].set_title('Average Processing Time per Production Stage', fontsize=14, fontweight='bold')
axs[1].set_ylabel('Average Processing Time (minutes)')
axs[1].grid(linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()
plt.show()