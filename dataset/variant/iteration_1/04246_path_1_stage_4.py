import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

countries = ["Country A", "Country B", "Country C", "Country D", "Country E", "Country F", "Country G", "Country H", "Country I", "Country J"]
researcher_density = np.array([8, 6, 15, 12, 17, 9, 11, 14, 10, 13])

fig, ax = plt.subplots(figsize=(12, 8))

# Change KDE plot to a horizontal one, with a different fill and color
sns.kdeplot(researcher_density, ax=ax, fill=True, color="darkorange", label="Researcher Density", linewidth=2)

# Change title and labels styling
ax.set_title("Innovator Density Across Nations", fontsize=18, fontweight='bold', color='darkred')
ax.set_xlabel("Innovation Density Index", fontsize=12, fontstyle='italic')
ax.set_ylabel("Density Distribution", fontsize=12, fontstyle='italic')

# Change legend title and styling
ax.legend(title="Plot Information", fontsize=11, title_fontsize='12', loc='upper right', shadow=True)

# Grid style changes
ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.8)

# Adjust tick style and border
ax.tick_params(axis='x', direction='in', length=6, width=1, colors='gray')
ax.tick_params(axis='y', direction='inout', length=6, width=1, colors='gray')

plt.tight_layout()
plt.show()