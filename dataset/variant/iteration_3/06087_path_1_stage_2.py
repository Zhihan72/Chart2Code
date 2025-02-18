import matplotlib.pyplot as plt
import numpy as np

# Define data
age_groups = ['Ch (6-12)', 'Teens (13-19)', 'Ad (20-39)', 'Mid-age (40-59)', 'Sr (60+)']
children = [1600, 1700, 1800, 1750, 1650, 1550, 1800, 1900, 2000, 1700]
teenagers = [2200, 2300, 2500, 2400, 2350, 2250, 2600, 2700, 2800, 2300]
adults = [2000, 2100, 2200, 2150, 2200, 2100, 2300, 2400, 2500, 2100]
middle_aged = [1800, 1900, 2000, 1950, 1850, 1750, 2000, 2100, 2200, 1900]
seniors = [1600, 1700, 1750, 1650, 1550, 1500, 1800, 1900, 2000, 1700]
all_data = [children, teenagers, adults, middle_aged, seniors]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the horizontal boxchart
bp = ax.boxplot(
    all_data, 
    vert=False, 
    patch_artist=True, 
    notch=False, 
    boxprops=dict(facecolor='#FFBB78', color='#FF7F0E'),
    whiskerprops=dict(color='#FF7F0E'), 
    capprops=dict(color='#FF7F0E'),
    medianprops=dict(color='purple', linestyle='--')
)

# Customize box colors
colors = ['#FF9896', '#C5B0D5', '#98DF8A', '#A0CBE8', '#FFBB78']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title('Caloric Intake in Age Groups - 2023', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Caloric Intake (kcal)', fontsize=13)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(age_groups, fontsize=13)

# Add grid
ax.grid(axis='y', linestyle='-', linewidth=0.5)

# Add mean markers
means = [np.mean(cat) for cat in all_data]
ax.scatter(means, range(1, len(age_groups) + 1), color='black', marker='s', label='Mean')

# Annotate max and min values
for i, cat in enumerate(all_data, start=1):
    min_val, max_val = min(cat), max(cat)
    ax.annotate(f'Min: {min_val}', xy=(min_val, i), xytext=(min_val-250, i-0.2),
                arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=10, color='orange')
    ax.annotate(f'Max: {max_val}', xy=(max_val, i), xytext=(max_val+60, i+0.2),
                arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()