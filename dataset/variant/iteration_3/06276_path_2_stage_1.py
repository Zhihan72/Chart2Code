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

# Create the plot with multiple subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 8))

# Box plot for the average daily steps
box = axs[0].boxplot(steps_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Apply a single color to all boxes
single_color = '#ff9999'
for patch in box['boxes']:
    patch.set_facecolor(single_color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

# Customize outliers
for flier in box['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# Customize plot elements
axs[0].set_yticklabels(programs, fontsize=11)
axs[0].set_xlabel('Average Daily Steps', fontsize=12)
axs[0].set_title('Analysis of Average Daily Steps\nAcross Different Health Programs', fontsize=14, fontweight='bold', pad=20)

# Bar plot showing the mean steps for each program
mean_steps = [np.mean(data) for data in steps_data]
axs[1].barh(programs, mean_steps, color=single_color, edgecolor='black')

# Customize plot elements
axs[1].set_xlabel('Average Daily Steps', fontsize=12)
axs[1].set_title('Mean Steps of Health Program Participants', fontsize=14, fontweight='bold', pad=20)

# Show mean values on bar chart
for i, v in enumerate(mean_steps):
    axs[1].text(v + 100, i, f'{v:.1f}', color='black', va='center', fontweight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()