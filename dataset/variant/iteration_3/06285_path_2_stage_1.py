import matplotlib.pyplot as plt

# Define ages for different fantasy game characters (in years)
elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]
dwarf_ages = [130, 135, 140, 145, 155, 160, 150, 145, 135, 150]
dragon_ages = [3000, 3200, 3100, 3300, 3400, 3500, 3450, 3550, 3600, 3250]
human_ages = [20, 22, 25, 30, 35, 40, 38, 32, 28, 24]
wizard_ages = [200, 220, 180, 210, 230, 220, 240, 250, 230, 260]

# Combine data into a list for plotting
age_data = [elf_ages, dwarf_ages, dragon_ages, human_ages, wizard_ages]

# Names for the categories
character_names = ["Elves", "Dwarves", "Dragons", "Humans", "Wizards"]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a vertical box plot
box = ax.boxplot(age_data, vert=True, patch_artist=True, 
                 labels=character_names,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkcyan', linewidth=1.5),
                 whiskerprops=dict(color='teal', linestyle='--'),
                 capprops=dict(color='teal'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

# Set colors for each box
colors = ['lightblue', 'lightsalmon', 'lightgreen', 'lightyellow', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add titles and axis labels
ax.set_title("Age Distribution of Fantasy Game Characters", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Age (years)", fontsize=14)
ax.set_xlabel("Character Type", fontsize=14)

# Annotate an interesting point
ax.annotate('Longest Lived Species',
            xy=(3, 3550),
            xytext=(2.5, 3600),
            arrowprops=dict(facecolor='navy', arrowstyle='->'),
            fontsize=12,
            color='navy')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()