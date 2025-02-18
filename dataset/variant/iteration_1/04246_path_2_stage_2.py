import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

countries = ["Land X", "Land Y", "Land Z", "Land W", "Land V", "Land U", "Land T", "Land S", "Land R", "Land Q"]
researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])
patents_filed = np.array([240, 180, 350, 300, 400, 220, 280, 370, 250, 330])

fig, ax = plt.subplots(figsize=(12, 8))

sns.kdeplot(y=researcher_density, ax=ax, fill=True, color="skyblue", label="Scholar Abundance")
sns.kdeplot(y=patents_filed, ax=ax, fill=True, color="coral", label="Inventions Created")

ax.set_title("Horizontal Density Chart", fontsize=16, fontweight='bold')
ax.set_xlabel("Density", fontsize=14)
ax.set_ylabel("Value", fontsize=14)
ax.legend(title="Profile", fontsize=12, title_fontsize='13')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()