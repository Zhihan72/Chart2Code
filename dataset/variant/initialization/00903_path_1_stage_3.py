import matplotlib.pyplot as plt
import numpy as np

# Data
countries = [
    "US", "Germany", "Canada", "UK", "Australia",
    "Japan", "S. Korea", "France", "China", "India"
]
education_percentages = [
    38.0, 31.0, 28.0, 29.0, 30.0,
    36.0, 34.0, 26.0, 20.0, 12.0
]
population_millions = [
    332.0, 83.2, 38.0, 67.2, 25.7,
    125.8, 51.7, 67.5, 1412.0, 1393.0
]

degree_holders_millions = [pop * (pct / 100) for pop, pct in zip(population_millions, education_percentages)]

# Predefined shuffled colors
colors = [
    (0.993248, 0.906157, 0.143936, 1.0),  # Example shuffled colors (originally from viridis)
    (0.267004, 0.004874, 0.329415, 1.0),
    (0.190631, 0.407061, 0.556089, 1.0),
    (0.20803, 0.718701, 0.472873, 1.0),
    (0.127568, 0.566949, 0.550556, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.287675, 0.76829, 0.499677, 1.0),
    (0.229739, 0.322361, 0.545706, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0)
]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Plot horizontal bar chart
bars = axes[0].barh(countries, education_percentages, color=colors, edgecolor='black', height=0.6)
axes[0].set_title('Bachelor\'s Degrees in 2022', fontsize=16, pad=20)
axes[0].set_xlabel('Percent (%)', fontsize=12)
axes[0].invert_yaxis()
axes[0].xaxis.grid(True, linestyle='--', alpha=0.7)

for bar in bars:
    width = bar.get_width()
    axes[0].text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', ha='left', fontsize=10)

# Plot donut pie chart
wedges, texts, autotexts = axes[1].pie(degree_holders_millions, labels=countries, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(width=0.3))
axes[1].set_title('Degree Holders (M) in 2022', fontsize=16, pad=20)

plt.tight_layout()
plt.subplots_adjust(wspace=0.3)

plt.show()