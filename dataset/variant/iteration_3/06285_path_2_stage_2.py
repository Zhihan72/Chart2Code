import matplotlib.pyplot as plt

# Randomly altered ages for different fantasy game characters (in years)
elf_ages = [510, 530, 535, 545, 565, 575, 585, 590, 580, 570]
dwarf_ages = [140, 140, 130, 155, 150, 165, 155, 145, 140, 145]
dragon_ages = [3100, 3250, 3400, 3350, 3500, 3450, 3550, 3600, 3000, 3200]
human_ages = [25, 27, 22, 35, 30, 38, 28, 32, 24, 20]
wizard_ages = [210, 220, 230, 200, 240, 250, 230, 260, 220, 180]

age_data = [elf_ages, dwarf_ages, dragon_ages, human_ages, wizard_ages]
character_names = ["Elves", "Dwarves", "Dragons", "Humans", "Wizards"]

fig, ax = plt.subplots(figsize=(10, 6))
box = ax.boxplot(age_data, vert=True, patch_artist=True, 
                 labels=character_names,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkcyan', linewidth=1.5),
                 whiskerprops=dict(color='teal', linestyle='--'),
                 capprops=dict(color='teal'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

colors = ['lightblue', 'lightsalmon', 'lightgreen', 'lightyellow', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_title("Age Distribution of Fantasy Game Characters", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Age (years)", fontsize=14)
ax.set_xlabel("Character Type", fontsize=14)

ax.annotate('Longest Lived Species',
            xy=(3, 3550),
            xytext=(2.5, 3600),
            arrowprops=dict(facecolor='navy', arrowstyle='->'),
            fontsize=12,
            color='navy')

plt.tight_layout()
plt.show()