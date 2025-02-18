import matplotlib.pyplot as plt

# A single group of ages data
elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]

fig, ax = plt.subplots(figsize=(8, 6))

# Plot a single vertical box chart for the elf ages
ax.boxplot(elf_ages, vert=True, patch_artist=True,
           flierprops=dict(marker='o', color='red', alpha=0.5),
           boxprops=dict(color='darkcyan', linewidth=1.5),
           whiskerprops=dict(color='teal', linestyle='--'),
           capprops=dict(color='teal'),
           medianprops=dict(color='orange', linewidth=2))

plt.show()