import matplotlib.pyplot as plt

elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]
dwarf_ages = [130, 135, 140, 145, 155, 160, 150, 145, 135, 150]
dragon_ages = [3000, 3200, 3100, 3300, 3400, 3500, 3450, 3550, 3600, 3250]
human_ages = [20, 22, 25, 30, 35, 40, 38, 32, 28, 24]
wizard_ages = [200, 220, 180, 210, 230, 220, 240, 250, 230, 260]

age_data = [elf_ages, dwarf_ages, dragon_ages, human_ages, wizard_ages]

fig, ax = plt.subplots(figsize=(14, 8))

ax.boxplot(age_data, vert=False, patch_artist=True, 
           flierprops=dict(marker='o', color='red', alpha=0.5),
           boxprops=dict(color='darkcyan', linewidth=1.5),
           whiskerprops=dict(color='teal', linestyle='--'),
           capprops=dict(color='teal'),
           medianprops=dict(color='orange', linewidth=2),
           notch=True)

plt.show()