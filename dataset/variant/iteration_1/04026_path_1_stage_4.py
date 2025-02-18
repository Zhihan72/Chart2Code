import matplotlib.pyplot as plt

popularity = [10, 40, 5, 20, 25]
colors = ['#ffcc99', '#ff6666', '#c2c2f0', '#99ff99', '#66b3ff']

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(popularity, colors=colors, startangle=140, explode=[0.1 if p == max(popularity) else 0 for p in popularity])

ax.axis('equal')
plt.tight_layout()
plt.show()