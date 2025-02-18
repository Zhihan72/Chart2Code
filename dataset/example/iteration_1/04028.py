import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Backstory: Comparing weather patterns in two fictional regions (Region Alpha and Region Beta)
# to analyze the density of temperature and rainfall over the year.

# Constructing explicit data
# Temperature data (in Celsius) over the course of a year
temperatures_alpha = np.array([
    7, 9, 11, 14, 18, 22, 25, 24, 20, 15, 10, 8,  # Region Alpha
    8, 11, 14, 17, 21, 26, 29, 28, 24, 19, 13, 9   # Region Beta
])

# Rainfall data (in mm) over the course of a year
rainfall_alpha = np.array([
    120, 110, 140, 90, 80, 70, 60, 50, 70, 80, 100, 130,  # Region Alpha
    100, 100, 120, 70, 60, 50, 40, 30, 40, 70, 90, 120    # Region Beta
])

# Month labels for the plot
months = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
])

# Normalize data for better density visualization
temperatures_alpha_norm = temperatures_alpha / temperatures_alpha.max()
rainfall_alpha_norm = rainfall_alpha / rainfall_alpha.max()

# Create a density plot
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Density of temperatures
sns.kdeplot(x=months, y=temperatures_alpha_norm[:12], ax=ax[0], fill=True, color='blue', alpha=0.6)
sns.kdeplot(x=months, y=temperatures_alpha_norm[12:], ax=ax[0], fill=True, color='red', alpha=0.6)
ax[0].set_title("Temperature Density Comparison\nRegion Alpha (Blue) vs Region Beta (Red)", fontsize=14, fontweight='bold')
ax[0].set_ylabel("Normalized Temperature", fontsize=12)

# Density of rainfall
sns.kdeplot(x=months, y=rainfall_alpha_norm[:12], ax=ax[1], fill=True, color='green', alpha=0.6)
sns.kdeplot(x=months, y=rainfall_alpha_norm[12:], ax=ax[1], fill=True, color='orange', alpha=0.6)
ax[1].set_title("Rainfall Density Comparison\nRegion Alpha (Green) vs Region Beta (Orange)", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Months", fontsize=12)
ax[1].set_ylabel("Normalized Rainfall", fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()