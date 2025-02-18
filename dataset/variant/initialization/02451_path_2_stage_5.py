import matplotlib.pyplot as plt
import numpy as np

categories = ['Action', 'Adventure', 'Strategy', 'Role-Playing', 'Simulation']
num_vars = len(categories)
ratings = [7.8, 8.3, 7.5, 8.0, 8.5]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
ratings += ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Randomly altered stylistic elements
ax.plot(angles, ratings, color='blue', linewidth=1.5, linestyle='--', marker='o', markersize=5)

# Show gridlines
ax.grid(True, linestyle='-', linewidth=0.5, color='gray')

# Changed border color and added title
ax.spines['polar'].set_edgecolor('red')
ax.set_title("Game Ratings", va='bottom')

# Added legend with altered style and position
ax.legend(['Ratings'], loc='upper right', fontsize='small', frameon=False)

plt.show()