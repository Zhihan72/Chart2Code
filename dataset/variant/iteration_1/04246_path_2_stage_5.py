import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])

fig, ax = plt.subplots(figsize=(12, 8))

sns.kdeplot(y=researcher_density, ax=ax, fill=True, color="mediumseagreen")

ax.set_title("Horizontal Density Chart", fontsize=16, fontweight='bold')
ax.set_xlabel("Density", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

plt.tight_layout()
plt.show()