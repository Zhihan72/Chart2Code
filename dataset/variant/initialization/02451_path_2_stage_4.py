import matplotlib.pyplot as plt
import numpy as np

categories = ['Action', 'Adventure', 'Strategy', 'Role-Playing', 'Simulation']
num_vars = len(categories)
ratings = [7.8, 8.3, 7.5, 8.0, 8.5]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
ratings += ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.plot(angles, ratings, color='green', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks([])
ax.set_xticklabels([])

plt.show()