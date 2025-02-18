import matplotlib.pyplot as plt

elf_ages = [510, 530, 535, 545, 565, 575, 585, 590, 580, 570]
dwarf_ages = [140, 140, 130, 155, 150, 165, 155, 145, 140, 145]
dragon_ages = [3100, 3250, 3400, 3350, 3500, 3450, 3550, 3600, 3000, 3200]
human_ages = [25, 27, 22, 35, 30, 38, 28, 32, 24, 20]
wizard_ages = [210, 220, 230, 200, 240, 250, 230, 260, 220, 180]

age_data = [elf_ages, dwarf_ages, dragon_ages, human_ages, wizard_ages]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(age_data, vert=True, patch_artist=True, boxprops=dict(facecolor='blue'))

plt.tight_layout()
plt.show()