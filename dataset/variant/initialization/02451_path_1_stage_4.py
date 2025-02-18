import matplotlib.pyplot as plt
import numpy as np

categories = ['Act', 'Adv', 'Strat', 'RPG', 'Sim']
num_vars = len(categories)

# Manually shuffled ratings to achieve a "random" order.
ratings = [7.5, 8.0, 8.3, 7.8, 8.5]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
ratings += ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.plot(angles, ratings, color='blue', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='darkblue')

plt.title('2023 Game Prefs', size=16, color='darkblue', y=1.1)

plt.show()