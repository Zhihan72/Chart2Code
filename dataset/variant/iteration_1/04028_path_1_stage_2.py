import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for three regions
temperatures_alpha = np.array([7, 9, 11, 14, 18, 22, 25, 24, 20, 15, 10, 8])
temperatures_beta = np.array([8, 11, 14, 17, 21, 26, 29, 28, 24, 19, 13, 9])
temperatures_gamma = np.array([5, 8, 12, 16, 20, 25, 28, 27, 23, 17, 12, 7])

rainfall_alpha = np.array([120, 110, 140, 90, 80, 70, 60, 50, 70, 80, 100, 130])
rainfall_beta = np.array([100, 100, 120, 70, 60, 50, 40, 30, 40, 70, 90, 120])
rainfall_gamma = np.array([130, 100, 150, 100, 90, 60, 50, 40, 50, 60, 110, 140])

# Month labels
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Normalize data
temperatures_alpha_norm = temperatures_alpha / temperatures_alpha.max()
temperatures_beta_norm = temperatures_beta / temperatures_beta.max()
temperatures_gamma_norm = temperatures_gamma / temperatures_gamma.max()

rainfall_alpha_norm = rainfall_alpha / rainfall_alpha.max()
rainfall_beta_norm = rainfall_beta / rainfall_beta.max()
rainfall_gamma_norm = rainfall_gamma / rainfall_gamma.max()

# Create horizontal density plot
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharey=True)

# Temperatures density plot
sns.kdeplot(y=months, x=temperatures_alpha_norm, ax=ax[0], fill=True, color='blue', alpha=0.6, label='Alpha')
sns.kdeplot(y=months, x=temperatures_beta_norm, ax=ax[0], fill=True, color='red', alpha=0.6, label='Beta')
sns.kdeplot(y=months, x=temperatures_gamma_norm, ax=ax[0], fill=True, color='purple', alpha=0.6, label='Gamma')
ax[0].set_title("Temperature Density Comparison\nAlpha (Blue), Beta (Red), Gamma (Purple)", fontsize=14, fontweight='bold')
ax[0].set_xlabel("Normalized Temperature", fontsize=12)
ax[0].legend()

# Rainfall density plot
sns.kdeplot(y=months, x=rainfall_alpha_norm, ax=ax[1], fill=True, color='green', alpha=0.6, label='Alpha')
sns.kdeplot(y=months, x=rainfall_beta_norm, ax=ax[1], fill=True, color='orange', alpha=0.6, label='Beta')
sns.kdeplot(y=months, x=rainfall_gamma_norm, ax=ax[1], fill=True, color='brown', alpha=0.6, label='Gamma')
ax[1].set_title("Rainfall Density Comparison\nAlpha (Green), Beta (Orange), Gamma (Brown)", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Normalized Rainfall", fontsize=12)
ax[1].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()