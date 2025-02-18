import matplotlib.pyplot as plt

# Define ages for different fantasy game characters (in years)
elf_ages = [500, 520, 530, 540, 560, 570, 590, 580, 575, 565]
dwarf_ages = [130, 135, 140, 145, 155, 160, 150, 145, 135, 150]
dragon_ages = [3000, 3200, 3100, 3300, 3400, 3500, 3450, 3550, 3600, 3250]
human_ages = [20, 22, 25, 30, 35, 40, 38, 32, 28, 24]
wizard_ages = [200, 220, 180, 210, 230, 220, 240, 250, 230, 260]

# Combine data into a list for plotting
age_data = [elf_ages, dwarf_ages, dragon_ages, human_ages, wizard_ages]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal box plot without labels and titles
box = ax.boxplot(age_data, vert=False, patch_artist=True, 
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

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()