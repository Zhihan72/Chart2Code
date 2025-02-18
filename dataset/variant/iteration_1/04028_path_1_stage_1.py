import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Temperature data (in Celsius) over the course of a year for three regions
temperatures_alpha = np.array([
    7, 9, 11, 14, 18, 22, 25, 24, 20, 15, 10, 8   # Region Alpha
])
temperatures_beta = np.array([
    8, 11, 14, 17, 21, 26, 29, 28, 24, 19, 13, 9  # Region Beta
])
temperatures_gamma = np.array([
    5, 8, 12, 16, 20, 25, 28, 27, 23, 17, 12, 7   # Region Gamma
])

# Rainfall data (in mm) over the course of a year for three regions
rainfall_alpha = np.array([
    120, 110, 140, 90, 80, 70, 60, 50, 70, 80, 100, 130  # Region Alpha
])
rainfall_beta = np.array([
    100, 100, 120, 70, 60, 50, 40, 30, 40, 70, 90, 120   # Region Beta
])
rainfall_gamma = np.array([
    130, 100, 150, 100, 90, 60, 50, 40, 50, 60, 110, 140 # Region Gamma
])

# Month labels for the plot
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Normalize data for better density visualization
temperatures_alpha_norm = temperatures_alpha / temperatures_alpha.max()
temperatures_beta_norm = temperatures_beta / temperatures_beta.max()
temperatures_gamma_norm = temperatures_gamma / temperatures_gamma.max()

rainfall_alpha_norm = rainfall_alpha / rainfall_alpha.max()
rainfall_beta_norm = rainfall_beta / rainfall_beta.max()
rainfall_gamma_norm = rainfall_gamma / rainfall_gamma.max()

# Create a density plot
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Density of temperatures
sns.kdeplot(x=months, y=temperatures_alpha_norm, ax=ax[0], fill=True, color='blue', alpha=0.6, label='Alpha')
sns.kdeplot(x=months, y=temperatures_beta_norm, ax=ax[0], fill=True, color='red', alpha=0.6, label='Beta')
sns.kdeplot(x=months, y=temperatures_gamma_norm, ax=ax[0], fill=True, color='purple', alpha=0.6, label='Gamma')
ax[0].set_title("Temperature Density Comparison\nAlpha (Blue), Beta (Red), Gamma (Purple)", fontsize=14, fontweight='bold')
ax[0].set_ylabel("Normalized Temperature", fontsize=12)
ax[0].legend()

# Density of rainfall
sns.kdeplot(x=months, y=rainfall_alpha_norm, ax=ax[1], fill=True, color='green', alpha=0.6, label='Alpha')
sns.kdeplot(x=months, y=rainfall_beta_norm, ax=ax[1], fill=True, color='orange', alpha=0.6, label='Beta')
sns.kdeplot(x=months, y=rainfall_gamma_norm, ax=ax[1], fill=True, color='brown', alpha=0.6, label='Gamma')
ax[1].set_title("Rainfall Density Comparison\nAlpha (Green), Beta (Orange), Gamma (Brown)", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Months", fontsize=12)
ax[1].set_ylabel("Normalized Rainfall", fontsize=12)
ax[1].legend()

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()