import matplotlib.pyplot as plt
import numpy as np

# Define technological advancements data
years = np.arange(3000, 3051, 10)
tech_advancement = {
    'AI and Robotics': np.array([10, 15, 20, 25, 35, 40]),
    'Sustainable Energy': np.array([5, 10, 15, 20, 30, 38]),
    'Biotechnology': np.array([8, 12, 18, 23, 27, 33]),
}

# Define new colors for line chart
line_colors = ['#FF4500', '#2E8B57', '#6A5ACD']

# Create the figure and axis for the line chart
fig, ax = plt.subplots(figsize=(9, 9))

# Plot the line chart for technological advancements
for (tech, improvements), color in zip(tech_advancement.items(), line_colors):
    ax.plot(years, improvements, label=tech, marker='o', linewidth=2.5, color=color)

# Customize line chart
ax.set_title('Technological Advancements (3000-3050)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Advancement Index', fontsize=12, fontweight='bold')
ax.legend(title="Technology Sectors", fontsize='medium', loc='best')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Layout and display
plt.tight_layout()
plt.show()