import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
contributions = np.array([90, 70, 130, 50, 110])  # Solar used as an example dataset
colors = ['#8B4513']

fig, ax = plt.subplots(figsize=(12, 7))

# Plot a simple vertical bar chart
ax.bar(years, contributions, color=colors[0], edgecolor='none', alpha=0.9)

ax.set_title("Renewables in GreenVille (2018-22)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Contribution (M USD)", fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()