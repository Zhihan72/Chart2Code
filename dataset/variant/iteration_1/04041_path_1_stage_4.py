import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

steps_friend_1 = [4100, 4350, 3600, 4900, 5400, 5900, 6050]
steps_friend_2 = [3450, 3750, 3150, 4200, 4550, 4500, 4850]
steps_friend_3 = [4400, 4750, 4950, 5250, 5600, 5750, 6100]
steps_friend_4 = [3050, 3200, 2800, 3550, 3700, 3950, 4050]

steps_data = np.array([steps_friend_1, steps_friend_2, steps_friend_3, steps_friend_4])

fig, ax = plt.subplots(figsize=(12, 8))

# Manually shuffled colors and different markers for variety
styles = [
    {'color': 'orange', 'marker': 'x', 'linestyle': ':'},
    {'color': 'cyan', 'marker': 's', 'linestyle': '-.'},
    {'color': 'magenta', 'marker': '^', 'linestyle': '--'},
    {'color': 'grey', 'marker': 'v', 'linestyle': '-'}
]

for i, steps in enumerate(steps_data):
    ax.plot(days, steps, marker=styles[i]['marker'], linestyle=styles[i]['linestyle'], color=styles[i]['color'])

# Randomized grid and border styles
ax.grid(True, linestyle='-', alpha=0.8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xticks(days)
ax.set_yticks(range(0, 7000, 500))
plt.xticks(rotation=30)
plt.tight_layout()

plt.show()