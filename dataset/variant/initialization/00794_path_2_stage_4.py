import matplotlib.pyplot as plt

color_usage = [20, 25, 18, 22, 15, 12, 8]
colors = ['#4682B4', '#FFD700', '#003366', '#8B0000', '#FFE4B5', '#FF6347', '#8A2BE2']

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