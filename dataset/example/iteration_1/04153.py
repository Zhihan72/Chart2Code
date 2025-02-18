import matplotlib.pyplot as plt
import numpy as np

# Context: Evolution of Artificial Intelligence (AI) Domain Development Over the Years
years = np.arange(2000, 2025)
# Data for different AI domains
machine_learning = np.array([2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278, 301])
natural_language_processing = np.array([1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256, 279])
computer_vision = np.array([1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278])
robotics = np.array([1, 2, 3, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256])
reinforcement_learning = np.array([1, 2, 3, 4, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157, 175, 194, 214, 235])

# Creating the cumulative sum for stacked area chart
cumulative_ai = machine_learning + natural_language_processing + computer_vision + robotics + reinforcement_learning

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area chart for AI domains
ax.stackplot(
    years,
    machine_learning,
    natural_language_processing,
    computer_vision,
    robotics,
    reinforcement_learning,
    labels=[
        'Machine Learning',
        'Natural Language Processing',
        'Computer Vision',
        'Robotics',
        'Reinforcement Learning'],
    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
    alpha=0.8
)

# Adding secondary axis for cumulative data
ax2 = ax.twinx()
ax2.plot(years, cumulative_ai, 'k--', linewidth=2, label='Total AI Development')

# Set the title and labels
ax.set_title(
    "Evolution of Artificial Intelligence (AI) Domain Development\n(2000-2025)",
    fontsize=18,
    fontweight='bold',
    pad=20
)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Development Effort (Unit)', fontsize=14)
ax2.set_ylabel('Total AI Development', fontsize=14, color='k')

# Enhance appearance
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', title='AI Domains', fontsize=11)
ax2.legend(loc='upper right')

# Automatically adjust layout
fig.tight_layout()

# Show plot
plt.show()