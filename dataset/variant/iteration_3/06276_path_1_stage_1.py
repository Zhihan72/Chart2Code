import matplotlib.pyplot as plt
import numpy as np

# Define health programs and fictional data (average daily steps)
programs = ['Morning Fitness', 'Evening Yoga', 'Weekend Hiking', 'Dance Workshops', 'Office Wellness']
steps_data = [
    [8500, 8700, 7800, 9000, 8800, 8900, 8600, 9100, 9200, 8450],  # Morning Fitness
    [4500, 4200, 4100, 4600, 4700, 4900, 4300, 4800, 4400, 4550],  # Evening Yoga
    [9500, 9600, 9400, 9300, 9200, 9800, 9900, 9700, 9350, 9600],  # Weekend Hiking
    [7000, 7500, 7200, 7100, 7350, 7600, 7800, 7400, 7500, 7350],  # Dance Workshops
    [5000, 4800, 4700, 5100, 5200, 5400, 4550, 4900, 5050, 5250]   # Office Wellness
]

# Create the plot with a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Box plot for the average daily steps
box = ax.boxplot(steps_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Define colors for each box
colors = ['#FFDDC1', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

# Customize outliers
for flier in box['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# Customize plot elements
ax.set_yticklabels(programs, fontsize=11)
ax.set_xlabel('Average Daily Steps', fontsize=12)
ax.set_title('Analysis of Average Daily Steps\nAcross Different Health Programs', fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()