import matplotlib.pyplot as plt
import numpy as np

modern_writers = ['Morrison', 'Atwood', 'Toni', 'Murakami', 'Rushdie']
modern_data = {
    'Morrison': [8, 9, 8, 5, 7],
    'Atwood': [7, 8, 7, 6, 8],
    'Toni': [6, 7, 9, 6, 7],
    'Murakami': [7, 7, 6, 8, 8],
    'Rushdie': [8, 8, 9, 4, 6]
}

categories = ['Creativity', 'Emotional Depth', 'Social Commentary', 'Humor', 'Style']
N = len(categories)

# Create subplots
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Set the angle for each axis
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Complete the loop at the end by appending the first angle to the end
angles += angles[:1]

for writer in modern_writers:
    values = modern_data[writer]
    # Complete the loop by appending the first value again
    values += values[:1]
    ax.fill(angles, values, alpha=0.25, label=writer)
    ax.plot(angles, values, linewidth=1, linestyle='solid')

# Add labels to the axes
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.tight_layout()
plt.show()