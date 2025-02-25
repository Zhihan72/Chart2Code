import matplotlib.pyplot as plt

popularity = [40, 25, 5, 7, 6, 4, 3, 3, 4, 3]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#c2c2f0', '#ffb3e6', '#ffcc99', '#b3b3cc', '#ffb366', '#c8e4ff', '#ff6666']
explode = (0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(popularity, explode=explode, colors=colors, startangle=140, wedgeprops=dict(edgecolor='w', linewidth=2))

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.set_aspect('equal')

plt.show()