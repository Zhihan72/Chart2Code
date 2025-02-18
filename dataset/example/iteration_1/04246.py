import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data: Researcher Density (researchers per 1,000 people) and Patents Filed (per million people)
countries = ["Country A", "Country B", "Country C", "Country D", "Country E", "Country F", "Country G", "Country H", "Country I", "Country J"]
researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])
patents_filed = np.array([240, 180, 350, 300, 400, 220, 280, 370, 250, 330])

fig, ax = plt.subplots(figsize=(12, 8))

# Kernel Density Estimation for density plot
sns.kdeplot(researcher_density, ax=ax, fill=True, color="skyblue", label="Researcher Density")
sns.kdeplot(patents_filed, ax=ax, fill=True, color="coral", label="Patents Filed")

ax.set_title("Correlation between Researcher Density and Patents Filed", fontsize=16, fontweight='bold')
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Density", fontsize=14)
ax.legend(title="Distribution", fontsize=12, title_fontsize='13')
ax.grid(True, linestyle='--', alpha=0.6)

# Additional Subplot: Scatter plot
scatter_ax = fig.add_axes([0.5, 0.5, 0.4, 0.4])
scatter_ax.scatter(researcher_density, patents_filed, color='purple', edgecolor='black', s=80, alpha=0.7)
for i, country in enumerate(countries):
    scatter_ax.text(researcher_density[i], patents_filed[i], country, fontsize=9, ha='right')
    
scatter_ax.set_title("Patents Filed vs Researcher Density", fontsize=12, fontweight='bold', pad=10)
scatter_ax.set_xlabel("Researcher Density (per 1000)", fontsize=10)
scatter_ax.set_ylabel("Patents Filed (per million)", fontsize=10)
scatter_ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()