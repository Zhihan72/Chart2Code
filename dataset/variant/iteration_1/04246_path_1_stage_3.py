import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

countries = ["Country A", "Country B", "Country C", "Country D", "Country E", "Country F", "Country G", "Country H", "Country I", "Country J"]
researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])

fig, ax = plt.subplots(figsize=(12, 8))

sns.kdeplot(researcher_density, ax=ax, fill=True, color="steelblue", label="Density of Researchers", vertical=True)

ax.set_title("Density of Researchers by Country", fontsize=16, fontweight='bold')
ax.set_xlabel("Probability Distribution", fontsize=14)
ax.set_ylabel("Innovator Density (per 1000)", fontsize=14)
ax.legend(title="Metrics Distribution", fontsize=12, title_fontsize='13')
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()