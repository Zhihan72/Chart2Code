import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6])
team_alpha = np.array([5, 10, 15, 20, 25, 30])
team_beta = np.array([7, 14, 21, 28, 35, 42])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, team_alpha, marker='o', linestyle='-', color='#FF5733', linewidth=2)
ax.plot(months, team_beta, marker='s', linestyle='--', color='#33FFBD', linewidth=2)

for (month, alpha_feat, beta_feat) in zip(months, team_alpha, team_beta):
    ax.annotate(f'{alpha_feat}', (month, alpha_feat), textcoords="offset points", xytext=(-10,10), ha='center')
    ax.annotate(f'{beta_feat}', (month, beta_feat), textcoords="offset points", xytext=(10,-15), ha='center')

ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Features Completed', fontsize=12, fontweight='bold')
ax.set_title('Feature Completion Trend (Jan-Jun)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])

plt.tight_layout()
plt.show()