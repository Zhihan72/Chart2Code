import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

population_density = [5000, 7000, 6000, 6500]

fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal density plot using seaborn
sns.kdeplot(y=population_density, ax=ax, fill=True, color='blue', alpha=0.6)

ax.grid(True, linestyle=':', alpha=0.5)

plt.ylim(4000, 7500)
plt.tight_layout()
plt.show()