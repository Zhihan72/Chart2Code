import matplotlib.pyplot as plt

# Original data for elf ages
elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]

# Additional data series for dwarves and humans
dwarf_ages = [250, 260, 255, 270, 265, 275, 280, 285, 290, 295]
human_ages = [30, 35, 40, 25, 45, 50, 55, 60, 65, 70]

# Combine all data series
ages_data = [elf_ages, dwarf_ages, human_ages]

fig, ax = plt.subplots(figsize=(10, 6))

# Create a boxplot for each age group
ax.boxplot(ages_data, vert=True, patch_artist=True,
           flierprops=dict(marker='o', color='purple', alpha=0.5),
           boxprops=dict(color='darkgreen', linewidth=1.5),
           whiskerprops=dict(color='navy', linestyle='--'),
           capprops=dict(color='navy'),
           medianprops=dict(color='maroon', linewidth=2))

# Set x-ticks for clarity
ax.set_xticklabels(['Elves', 'Dwarves', 'Humans'])

plt.show()