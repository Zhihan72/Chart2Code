import numpy as np
import matplotlib.pyplot as plt

aspects = ['Speed', 'Accuracy', 'Memory Usage', 'Battery Life', 'Latency', 'Scalability']
data = [
    [85, 70, 60, 75, 90, 65],
    [80, 75, 70, 65, 85, 60],
    [75, 80, 85, 70, 80, 75],
    [70, 65, 80, 80, 75, 85],
    [88, 77, 69, 74, 91, 67]
]

names = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
colors = ['#2E8B57', '#FF6347', '#1E90FF', '#FFD700', '#FF69B4']

angles = np.linspace(0, 2 * np.pi, len(aspects), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for scores, name, color in zip(data, names, colors):
    scores += scores[:1]
    ax.fill(angles, scores, color=color, alpha=0.3, label=name)
    ax.plot(angles, scores, linewidth=2, linestyle='dashdot', marker='o', markersize=6, color=color)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(aspects)
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)))

plt.title('Tech Giant Performance Comparison in 2023', y=1.1)

ax.legend(loc='lower left', bbox_to_anchor=(-0.2, 0.2), frameon=False)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()