import numpy as np
import matplotlib.pyplot as plt

# Define performance aspects and scores
aspects = ['Speed', 'Accuracy', 'Memory Usage', 'Battery Life', 'Latency', 'Scalability']
data = [
    [85, 70, 60, 75, 90, 65],
    [80, 75, 70, 65, 85, 60],
    [75, 80, 85, 70, 80, 75],
    [70, 65, 80, 80, 75, 85],
    [88, 77, 69, 74, 91, 67]
]

# Company names and colors
names = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
colors = ['#2E8B57', '#FF6347', '#1E90FF', '#FFD700', '#FF69B4']

# Calculate angles for the radar plot
angles = np.linspace(0, 2 * np.pi, len(aspects), endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart (fill-area radar chart)
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Fill and plot each company's data
for scores, name, color in zip(data, names, colors):
    scores += scores[:1]  # Close the loop
    ax.fill(angles, scores, color=color, alpha=0.25, label=name)
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=color)

# Configure chart
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(aspects)
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)))

# Title and legend
plt.title('Tech Giant Performance Comparison in 2023', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()