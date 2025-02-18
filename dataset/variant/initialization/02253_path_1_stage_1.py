import numpy as np
import matplotlib.pyplot as plt

# Define decades
decades = np.arange(2100, 2210, 10)

# Artificial data for technological innovations (arbitrary units)
robotics = [5, 12, 30, 60, 100, 150, 220, 300, 380, 480, 600]
space_travel = [60, 90, 120, 150, 160, 170, 180, 190, 195, 200, 210]
quantum_computing = [4, 10, 18, 30, 50, 80, 130, 190, 270, 350, 450]
cybernetics = [25, 40, 70, 90, 115, 130, 160, 210, 260, 320, 380]

# Stack data for plotting
data = np.array([robotics, space_travel, quantum_computing, cybernetics])

# Colors for each technological innovation
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371']

# Calculate total technological advancements
total_innovations = np.sum(data, axis=0)

# Plot setup with 1 row and 2 columns
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Stackplot for technological innovations
axs[0].stackplot(decades, data, labels=['Robotics', 'Space Travel', 'Quantum Computing', 'Cybernetics'],
                 colors=colors, alpha=0.8)
axs[0].plot(decades, total_innovations, label='Total Technological Advancements',
            color='black', linestyle='--', marker='o', linewidth=2)

# Title and labels for the first plot
axs[0].set_title('Technological Innovations Over a Century\nin the Fictional Galaxy', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Decade', fontsize=12)
axs[0].set_ylabel('Innovation Units', fontsize=12)
axs[0].legend(loc='upper left', title='Technological Sectors', fontsize=10, title_fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Annotate significant points in the first plot
max_robotics_decade = np.argmax(robotics) * 10 + 2100
max_robotics_value = max(robotics)
axs[0].annotate(f'Max Robotics\n{max_robotics_value} units',
                xy=(max_robotics_decade, max_robotics_value),
                xytext=(max_robotics_decade + 5, max_robotics_value + 100),
                arrowprops=dict(facecolor='red', arrowstyle='->'),
                fontsize=10, color='red', fontweight='bold')

max_total_decade = np.argmax(total_innovations) * 10 + 2100
max_total_value = max(total_innovations)
axs[0].annotate(f'Peak Total\n{max_total_value} units',
                xy=(max_total_decade, max_total_value),
                xytext=(max_total_decade, max_total_value + 150),
                arrowprops=dict(facecolor='blue', arrowstyle='->'),
                fontsize=10, color='blue', fontweight='bold')

# Total growth for each category across the decades
total_growth = np.sum(np.diff(data) / data[:, :-1] * 100, axis=1)
sector_labels = ['Robotics', 'Space Travel', 'Quantum Computing', 'Cybernetics']

# Sort growth for bar chart
sorted_indices = np.argsort(total_growth)[::-1]  # to sort in descending order
sorted_growth = total_growth[sorted_indices]
sorted_labels = [sector_labels[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]

# Bar plot for sorted growth rates
axs[1].bar(sorted_labels, sorted_growth, color=sorted_colors, alpha=0.7)

# Title and labels for the second plot
axs[1].set_title('Total Growth Rate of Technological Innovations\nSorted by Sector', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Technological Sectors', fontsize=12)
axs[1].set_ylabel('Total Growth Rate (%)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Display the plot
plt.show()