import matplotlib.pyplot as plt
import numpy as np

body_assembly = [46, 49, 47, 51, 50, 48, 45, 52, 48, 46, 47, 50, 51, 50, 49, 46, 50, 52]
painting = [31, 35, 32, 34, 33, 31, 34, 30, 32, 33, 32, 34, 30, 32, 31, 30, 33, 35]
engine_installation = [61, 67, 62, 65, 63, 64, 66, 67, 65, 61, 62, 66, 64, 63, 65, 66, 62, 63]
interior_assembly = [41, 43, 40, 42, 39, 42, 41, 39, 43, 40, 42, 41, 40, 42, 43, 39, 43, 42]
quality_control = [21, 24, 22, 23, 21, 24, 20, 22, 23, 20, 22, 21, 24, 23, 20, 22, 23, 21]

data = [body_assembly, painting, engine_installation, interior_assembly, quality_control]

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

axs[0].boxplot(data, vert=False, patch_artist=True, notch=True,
               boxprops=dict(facecolor="lightsalmon", color="darkgreen"),
               whiskerprops=dict(color="darkorange"),
               capprops=dict(color="darkcyan"),
               medianprops=dict(color="darkblue"),
               flierprops=dict(markerfacecolor='gold', marker='o', alpha=0.5))

average_processing_time = [np.mean(stage) for stage in data]
stage_indices = np.arange(len(data))

axs[1].bar(stage_indices, average_processing_time, color='peru', edgecolor='navy')

plt.tight_layout()
plt.show()