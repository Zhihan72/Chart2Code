import matplotlib.pyplot as plt

color_usage = [20, 25, 18, 22, 15, 12, 8]
# New set of colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(10, 8))
wedges = ax.pie(
    color_usage,
    startangle=90,
    colors=colors,
    shadow=True,
    explode=(0.05,) * len(color_usage)
)

ax.axis('equal')

plt.tight_layout()

plt.show()