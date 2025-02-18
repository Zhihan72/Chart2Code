import matplotlib.pyplot as plt
import numpy as np

# Define labels for chart axes
disciplines = ['Sciences', 'Engineering', 'Humanities', 'Social Sciences']
funding_sources = ['Government Grants', 'Private Sector', 'University Funds', 'Non-Profit Organizations']

# Randomly altered funding amounts within each discipline, maintaining structure
funding_data = np.array([
    [20, 60, 10, 30],
    [30, 15, 70, 20],
    [30, 20, 10, 40],
    [15, 20, 40, 25],
])

num_disciplines = len(disciplines)
num_sources = len(funding_sources)

bar_width = 0.2

# Colors remain associated with the funding sources
colors = ['#ff7f0e', '#2ca02c', '#d62728', '#1f77b4']

fig, ax = plt.subplots(figsize=(10, 7))
index = np.arange(num_disciplines)

for i in range(num_sources):
    ax.bar(index + i * bar_width, funding_data[:, i], width=bar_width, color=colors[i], alpha=0.85)

ax.set_yticks(np.arange(0, 81, 10))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()