import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
interest_data = {
    'Coding': np.array([6, 7, 8, 8, 9, 9, 7, 6, 7, 8, 8, 9]),
    'Cooking': np.array([5, 6, 6, 8, 9, 9, 8, 7, 6, 6, 7, 8]),
    'Gardening': np.array([4, 5, 6, 7, 8, 9, 9, 7, 6, 5, 4, 4]),
    'Hiking': np.array([7, 6, 7, 9, 10, 9, 8, 7, 7, 7, 6, 7]),
    'Reading': np.array([8, 8, 9, 9, 10, 10, 8, 8, 9, 10, 10, 9])
}

colors = {
    'Coding': 'blue',
    'Cooking': 'orange',
    'Gardening': 'green',
    'Hiking': 'red',
    'Reading': 'purple'
}

fig, ax = plt.subplots(figsize=(14, 7))
for hobby, interest in interest_data.items():
    ax.plot(months, interest, marker='o', color=colors[hobby], linewidth=2)

peak_annotations = {
    'Coding': [(4, 'Hackathon Month')],
    'Cooking': [(5, 'Cooking Competition')],
    'Gardening': [(8, 'Harvest Month')],
    'Hiking': [(4, 'Spring Break'), (5, 'Perfect Weather')],
    'Reading': [(9, 'Book Club Month')]
}

for hobby, peaks in peak_annotations.items():
    for m_idx, label in peaks:
        ax.annotate(label,
                    xy=(months[m_idx-1], interest_data[hobby][m_idx-1]),
                    xytext=(months[m_idx-1], interest_data[hobby][m_idx-1] + 1),
                    arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                    fontsize=10, color=colors[hobby])

ax.set_title('Community Interest Levels in Hobbies Over 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Interest Level (1-10)', fontsize=12)
ax.set_xticks(months)
ax.set_yticks(np.arange(0, 11, 1))

# Removing legend, grid, and other stylistic elements such as borders are inherently not drawn.

plt.tight_layout()
plt.show()