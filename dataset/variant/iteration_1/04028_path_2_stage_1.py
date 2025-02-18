import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Preparing data
temperatures_alpha = np.array([
    7, 9, 11, 14, 18, 22, 25, 24, 20, 15, 10, 8, 
    8, 11, 14, 17, 21, 26, 29, 28, 24, 19, 13, 9  
])

rainfall_alpha = np.array([
    120, 110, 140, 90, 80, 70, 60, 50, 70, 80, 100, 130, 
    100, 100, 120, 70, 60, 50, 40, 30, 40, 70, 90, 120    
])

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Normalize data
temperatures_alpha_norm = temperatures_alpha / temperatures_alpha.max()
rainfall_alpha_norm = rainfall_alpha / rainfall_alpha.max()

# Create plots
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot temperature density
sns.kdeplot(x=months, y=temperatures_alpha_norm[:12], ax=ax[0], fill=True, color='blue', alpha=0.6)
sns.kdeplot(x=months, y=temperatures_alpha_norm[12:], ax=ax[0], fill=True, color='red', alpha=0.6)
ax[0].set_title("Temp Density: Alpha vs Beta", fontsize=14, fontweight='bold')
ax[0].set_ylabel("Norm Temp", fontsize=12)

# Plot rainfall density
sns.kdeplot(x=months, y=rainfall_alpha_norm[:12], ax=ax[1], fill=True, color='green', alpha=0.6)
sns.kdeplot(x=months, y=rainfall_alpha_norm[12:], ax=ax[1], fill=True, color='orange', alpha=0.6)
ax[1].set_title("Rain Density: Alpha vs Beta", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Month", fontsize=12)
ax[1].set_ylabel("Norm Rain", fontsize=12)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display
plt.show()