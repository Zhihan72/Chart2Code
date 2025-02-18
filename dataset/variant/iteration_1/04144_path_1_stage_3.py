import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6])
team_alpha = np.array([6, 11, 16, 22, 26, 31])  # Manually altered values
team_beta = np.array([8, 13, 23, 30, 36, 40])   # Manually altered values
team_gamma = np.array([5, 8, 13, 19, 25, 28])   # Manually altered values

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, team_alpha, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Alpha')
ax.plot(months, team_beta, marker='s', linestyle='--', color='#33FFBD', linewidth=2, label='Beta')
ax.plot(months, team_gamma, marker='^', linestyle='-.', color='#335BFF', linewidth=2, label='Gamma')

for (month, alpha_feat, beta_feat, gamma_feat) in zip(months, team_alpha, team_beta, team_gamma):
    ax.annotate(f'{alpha_feat}', (month, alpha_feat), textcoords="offset points", xytext=(-10,10), ha='center')
    ax.annotate(f'{beta_feat}', (month, beta_feat), textcoords="offset points", xytext=(10,-15), ha='center')
    ax.annotate(f'{gamma_feat}', (month, gamma_feat), textcoords="offset points", xytext=(-10,-20), ha='center')

ax.set_xlabel('Mth', fontsize=12, fontweight='bold')
ax.set_ylabel('Features', fontsize=12, fontweight='bold')
ax.set_title('Trend Jan-Jun', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
ax.legend()

plt.show()