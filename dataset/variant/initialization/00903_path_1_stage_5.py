import matplotlib.pyplot as plt

countries = [
    "US", "Germany", "Canada", "UK", "Australia",
    "Japan", "S. Korea", "France", "China", "India"
]
education_percentages = [
    38.0, 31.0, 28.0, 29.0, 30.0,
    36.0, 34.0, 26.0, 20.0, 12.0
]

colors = [
    (0.993248, 0.906157, 0.143936, 1.0),
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

fig, ax = plt.subplots(figsize=(9, 8))

bars = ax.barh(countries, education_percentages, color=colors, edgecolor='black', height=0.6)
ax.set_xlabel('Percent (%)', fontsize=12)
ax.invert_yaxis()

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', ha='left', fontsize=10)

plt.tight_layout()
plt.show()