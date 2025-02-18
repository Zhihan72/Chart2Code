import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

countries = ["Country A", "Country B", "Country C", "Country D", "Country E", "Country F", "Country G", "Country H", "Country I", "Country J"]
researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])
patents_filed = np.array([240, 180, 350, 300, 400, 220, 280, 370, 250, 330])

fig, ax = plt.subplots(figsize=(12, 8))

# Switching colors and labels in KDE plots
sns.kdeplot(researcher_density, ax=ax, fill=True, color="coral", label="Density of Researchers")
sns.kdeplot(patents_filed, ax=ax, fill=True, color="skyblue", label="Filed Patents")

# Altering titles, labels, and legend
ax.set_title("Linkage of Innovators and Patents", fontsize=16, fontweight='bold')
ax.set_xlabel("Metrics", fontsize=14)
ax.set_ylabel("Probability Distribution", fontsize=14)
ax.legend(title="Metrics Distribution", fontsize=12, title_fontsize='13')
ax.grid(True, linestyle='--', alpha=0.6)

# Additional Subplot: Scatter plot
scatter_ax = fig.add_axes([0.5, 0.5, 0.4, 0.4])
scatter_ax.scatter(researcher_density, patents_filed, color='purple', edgecolor='black', s=80, alpha=0.7)
for i, country in enumerate(countries):
    scatter_ax.text(researcher_density[i], patents_filed[i], country, fontsize=9, ha='right')
    
# Renaming scatter plot titles and labels
scatter_ax.set_title("Innovation by Innovators' Spread", fontsize=12, fontweight='bold', pad=10)
scatter_ax.set_xlabel("Innovator Density (per 1000)", fontsize=10)
scatter_ax.set_ylabel("Innovations (per million)", fontsize=10)
scatter_ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()