import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)

machine_learning = np.array([3, 8, 38, 47, 5, 30, 23, 233, 68, 2, 17, 12, 212, 301, 57, 93, 122, 192, 107, 138, 173, 255, 278, 155, 80])
natural_language_processing = np.array([58, 31, 123, 2, 9, 234, 139, 13, 81, 213, 193, 4, 48, 256, 213, 156, 1, 69, 108, 174, 279, 24, 39, 18, 94])
computer_vision = np.array([68, 38, 1, 80, 12, 5, 233, 47, 138, 2, 8, 30, 3, 278, 173, 122, 212, 17, 192, 57, 93, 107, 155, 23, 255])
robotics = np.array([193, 69, 94, 31, 123, 1, 56, 139, 9, 24, 18, 174, 213, 256, 234, 58, 108, 81, 13, 48, 39, 6, 3, 213, 4])
reinforcement_learning = np.array([7, 49, 1, 235, 40, 3, 140, 5, 157, 95, 19, 175, 109, 214, 32, 70, 4, 22, 124, 14, 10, 25, 82, 194, 59])

cumulative_ai = machine_learning + natural_language_processing + computer_vision + robotics + reinforcement_learning

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(
    years,
    machine_learning,
    natural_language_processing,
    computer_vision,
    robotics,
    reinforcement_learning,
    labels=['ML', 'NLP', 'CV', 'Robotics', 'RL'],
    # Shuffled colors for different data groups
    colors=['#d62728', '#1f77b4', '#2ca02c', '#9467bd', '#ff7f0e'],
    alpha=0.7
)

ax2 = ax.twinx()
ax2.plot(years, cumulative_ai, 'm-.', linewidth=2, label='Total AI Dev')

ax.set_title("AI Domain Growth (2000-2025)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Dev Effort', fontsize=14)
ax2.set_ylabel('Total AI Dev', fontsize=14, color='m')

ax.grid(True, linestyle=':', alpha=0.4)
ax.legend(loc='upper left', title='Domains', fontsize=11)
ax2.legend(loc='upper right')

fig.tight_layout()

plt.show()