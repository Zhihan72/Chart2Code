import numpy as np
import matplotlib.pyplot as plt

aspects = ['Speed', 'Accuracy', 'Memory Usage', 'Battery Life', 'Latency', 'Scalability']
num_aspects = len(aspects)

companyA_scores = [85, 70, 60, 75, 90, 65]
companyB_scores = [80, 75, 70, 65, 85, 60]
companyC_scores = [75, 80, 85, 70, 80, 75]
companyD_scores = [70, 65, 80, 80, 75, 85]
companyE_scores = [90, 60, 75, 80, 70, 66]
companyF_scores = [65, 85, 70, 60, 65, 80]

data = [companyA_scores, companyB_scores, companyC_scores, companyD_scores, companyE_scores, companyF_scores]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#4B0082', '#FF4500']

angles = np.linspace(0, 2 * np.pi, num_aspects, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for scores, color in zip(data, colors):
    scores += scores[:1]
    ax.fill(angles, scores, color=color, alpha=0.25)
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=color)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(aspects, fontsize=10)

ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)), fontsize=8)

plt.title('Tech Giant Performance Comparison in 2023\nEvaluating Key Performance Metrics', size=15, color='navy', y=1.1, ha='center')

plt.tight_layout()
plt.show()