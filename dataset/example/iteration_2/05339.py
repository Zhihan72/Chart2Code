import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In a growing city, there is increasing interest in the health implications of different diets. 
# Researchers gathered data on monthly cholesterol levels for individuals following different diets over a year.
# The diets under comparison are Vegetarian, Vegan, Paleo, Mediterranean, and Standard Western.

# Constructed data (cholesterol levels in mg/dL)
diets = ['Vegetarian', 'Vegan', 'Paleo', 'Mediterranean', 'Standard Western']
cholesterol_levels = {
    'Vegetarian': [180, 190, 185, 195, 178, 182, 188, 185, 192, 190, 186, 184],
    'Vegan': [170, 160, 165, 155, 168, 162, 158, 164, 170, 165, 160, 167],
    'Paleo': [220, 215, 210, 205, 198, 200, 202, 207, 215, 213, 209, 217],
    'Mediterranean': [195, 190, 192, 185, 187, 189, 192, 195, 200, 188, 190, 193],
    'Standard Western': [230, 240, 235, 245, 238, 242, 239, 247, 250, 245, 248, 240]
}

# Convert the data into a list of arrays for plotting
data = [np.array(cholesterol_levels[diet]) for diet in diets]

# Create a figure with a specific size
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Plot 1: Horizontal box plot for cholesterol levels
bplot1 = axes[0].boxplot(data, vert=False, patch_artist=True, labels=diets, notch=True, whis=1.5)

# Define colors for each diet
colors = ['#FFCC33', '#33CC99', '#FF6633', '#3399FF', '#CC3333']
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Customize whiskers, caps, medians, and fliers for better aesthetics and readability
for whisker in bplot1['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')

for cap in bplot1['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in bplot1['medians']:
    median.set(color='black', linewidth=2)

for flier in bplot1['fliers']:
    flier.set(marker='o', color='#FF33CC', alpha=0.5)

axes[0].set_title('Variability in Cholesterol Levels by Diet\nOver One Year', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Cholesterol Level (mg/dL)', fontsize=12)
axes[0].set_ylabel('Diet Types', fontsize=12)
axes[0].grid(True, linestyle='--', which='both', alpha=0.7)

# Compute mean cholesterol levels for the summary line plot
mean_cholesterol = [np.mean(levels) for levels in data]

# Plot 2: Line plot for mean cholesterol levels
axes[1].plot(diets, mean_cholesterol, marker='o', color='b', linestyle='-', linewidth=2, markersize=10)
axes[1].set_title('Mean Cholesterol Levels by Diet', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Diet Types', fontsize=12)
axes[1].set_ylabel('Mean Cholesterol Level (mg/dL)', fontsize=12)
axes[1].set_ylim(160, 260)

# Annotate each mean value on the line plot
for i, mean_val in enumerate(mean_cholesterol):
    axes[1].annotate(f'{mean_val:.1f}', (diets[i], mean_val),
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Improve layout to avoid overlaps and occlusions
plt.tight_layout()

# Display the plot
plt.show()