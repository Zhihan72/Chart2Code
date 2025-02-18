import matplotlib.pyplot as plt
import numpy as np

# Define the genres
categories = ['Action', 'Adventure', 'Strategy', 'Role-Playing', 'Simulation']
num_vars = len(categories)
ratings = [8.5, 7.8, 8.0, 8.3, 7.5]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
ratings += ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.fill(angles, ratings, color='skyblue', alpha=0.4)
ax.plot(angles, ratings, color='blue', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks([])
ax.set_xticklabels([])

plt.show()