import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Preparing data
temperatures_alpha = np.array([
    7, 9, 11, 14, 18, 22, 25, 24, 20, 15, 10, 8, 
    8, 11, 14, 17, 21, 26, 29, 28, 24, 19, 13, 9
])

temperatures_gamma = np.array([
    5, 6, 8, 12, 15, 19, 23, 22, 18, 12, 7, 6, 
    6, 9, 12, 16, 19, 23, 27, 26, 22, 17, 11, 7
])

rainfall_alpha = np.array([
    120, 110, 140, 90, 80, 70, 60, 50, 70, 80, 100, 130, 
    100, 100, 120, 70, 60, 50, 40, 30, 40, 70, 90, 120
])

rainfall_gamma = np.array([
    130, 120, 150, 100, 90, 80, 70, 60, 80, 90, 110, 140, 
    110, 110, 130, 80, 70, 60, 50, 40, 50, 80, 100, 130
])

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Normalize data
temperatures_alpha_norm = temperatures_alpha / temperatures_alpha.max()
temperatures_gamma_norm = temperatures_gamma / temperatures_gamma.max()
rainfall_alpha_norm = rainfall_alpha / rainfall_alpha.max()
rainfall_gamma_norm = rainfall_gamma / rainfall_gamma.max()

# Create plots
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharey=True)

# Plot horizontal temperature density
sns.kdeplot(y=months, x=temperatures_alpha_norm[:12], ax=ax[0], fill=True, color='cyan', alpha=0.5, label='Alpha', linestyle='--', marker='o')
sns.kdeplot(y=months, x=temperatures_alpha_norm[12:], ax=ax[0], fill=True, color='magenta', alpha=0.5, label='Beta', linestyle='-.', marker='s')
sns.kdeplot(y=months, x=temperatures_gamma_norm[:12], ax=ax[0], fill=True, color='lime', alpha=0.5, label='Gamma', linestyle=':', marker='^')
ax[0].set_title("Temp Density: Alpha vs Beta vs Gamma", fontsize=15, fontweight='bold')
ax[0].set_xlabel("Density")
ax[0].set_ylabel("Month")

# Plot horizontal rainfall density
sns.kdeplot(y=months, x=rainfall_alpha_norm[:12], ax=ax[1], fill=True, color='gold', alpha=0.5, label='Alpha', linestyle='-', marker='x')
sns.kdeplot(y=months, x=rainfall_alpha_norm[12:], ax=ax[1], fill=True, color='darkorange', alpha=0.5, label='Beta', linestyle=':', marker='+')
sns.kdeplot(y=months, x=rainfall_gamma_norm[:12], ax=ax[1], fill=True, color='darkred', alpha=0.5, label='Gamma', linestyle='-', marker='d')
ax[1].set_title("Rain Density: Alpha vs Beta vs Gamma", fontsize=15, fontweight='bold')
ax[1].set_xlabel("Density")

# Adjust legend and grid
for a in ax:
    a.legend(loc='upper right', fontsize=10, frameon=False)
    a.grid(linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()