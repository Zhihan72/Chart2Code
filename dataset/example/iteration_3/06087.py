import matplotlib.pyplot as plt
import numpy as np

# Backstory: Caloric Intake of Different Age Groups
# In 2023, a nationwide health survey was conducted to analyze the caloric intake habits across different age groups.
# The purpose was to understand dietary habits and provide insights for public health initiatives.

# Define age groups
age_groups = ['Children (6-12)', 'Teenagers (13-19)', 'Adults (20-39)', 'Middle-aged (40-59)', 'Senior (60+)']

# Caloric intake data (in kcal) for each age group
children = [1600, 1700, 1800, 1750, 1650, 1550, 1800, 1900, 2000, 1700]
teenagers = [2200, 2300, 2500, 2400, 2350, 2250, 2600, 2700, 2800, 2300]
adults = [2000, 2100, 2200, 2150, 2200, 2100, 2300, 2400, 2500, 2100]
middle_aged = [1800, 1900, 2000, 1950, 1850, 1750, 2000, 2100, 2200, 1900]
seniors = [1600, 1700, 1750, 1650, 1550, 1500, 1800, 1900, 2000, 1700]

# Combine data into a list for the box plot
all_data = [children, teenagers, adults, middle_aged, seniors]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the horizontal box chart
bp = ax.boxplot(
    all_data, 
    vert=False, 
    patch_artist=True, 
    notch=True, 
    boxprops=dict(facecolor='#A0CBE8', color='#1F77B4'),
    whiskerprops=dict(color='#1F77B4'), 
    capprops=dict(color='#1F77B4'),
    medianprops=dict(color='red')
)

# Customize the colors of each box
colors = ['#A0CBE8', '#FFBB78', '#98DF8A', '#FF9896', '#C5B0D5']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title(
    'Nationwide Survey on Caloric Intake in Different Age Groups for 2023', 
    fontsize=16, 
    fontweight='bold', 
    pad=20
)
ax.set_xlabel('Caloric Intake (kcal)', fontsize=12)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(age_groups, fontsize=12)

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add mean markers
means = [np.mean(cat) for cat in all_data]
ax.scatter(means, range(1, len(age_groups) + 1), color='blue', marker='D', label='Mean Value')

# Annotate maximum and minimum values for each category
for i, cat in enumerate(all_data, start=1):
    min_val, max_val = min(cat), max(cat)
    ax.annotate(f'Min: {min_val}', xy=(min_val, i), xytext=(min_val-200, i-0.3),
                arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green')
    ax.annotate(f'Max: {max_val}', xy=(max_val, i), xytext=(max_val+50, i+0.1),
                arrowprops=dict(facecolor='red', shrink=0.05), fontsize=9, color='red')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()