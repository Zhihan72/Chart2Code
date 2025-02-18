import numpy as np
import matplotlib.pyplot as plt

# Altering aspects list - these are the radial categories
aspects = ['Latency', 'Battery Life', 'Memory Usage', 'Speed', 'Scalability', 'Accuracy']
num_aspects = len(aspects)

# Renaming the scores of companies, assuming they represent different companies now
companyX_scores = [85, 70, 60, 75, 90, 65]
companyY_scores = [80, 75, 70, 65, 85, 60]
companyZ_scores = [75, 80, 85, 70, 80, 75]
companyW_scores = [70, 65, 80, 80, 75, 85]
companyV_scores = [90, 60, 75, 80, 70, 66]
companyU_scores = [65, 85, 70, 60, 65, 80]

data = [companyX_scores, companyY_scores, companyZ_scores, companyW_scores, companyV_scores, companyU_scores]

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

# Altering the plot title and subtitle
plt.title('2023 Performance Scale of Tech Behemoths\nKey Indicator Review', size=15, color='navy', y=1.1, ha='center')

plt.tight_layout()
plt.show()