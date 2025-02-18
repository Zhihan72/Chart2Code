import matplotlib.pyplot as plt

elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]

fig, ax = plt.subplots(figsize=(8, 6))

ax.boxplot(elf_ages, vert=True, patch_artist=True,
           flierprops=dict(marker='o', color='purple', alpha=0.5),
           boxprops=dict(color='darkgreen', linewidth=1.5),
           whiskerprops=dict(color='navy', linestyle='--'),
           capprops=dict(color='navy'),
           medianprops=dict(color='maroon', linewidth=2))

plt.show()