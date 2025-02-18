import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))

# Original data - modified step with shuffling
espresso_consumption = 220 + 50 * np.sin(np.linspace(0, 4 * np.pi, 52)) + np.linspace(0, 10, 52)
french_press_consumption = 200 + 45 * np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 8) + np.linspace(5, 15, 52)
americano_consumption = 180 + 40 * np.sin(np.linspace(0, 4 * np.pi, 52) - np.pi / 6) + np.linspace(10, 20, 52)

# Shuffling the data within its own structure
shuffled_espresso_consumption = np.random.permutation(espresso_consumption)
shuffled_french_press_consumption = np.random.permutation(french_press_consumption)
shuffled_americano_consumption = np.random.permutation(americano_consumption)

# Sorting the data in ascending order
sorted_espresso_weeks = weeks[np.argsort(shuffled_espresso_consumption)]
sorted_espresso_consumption = np.sort(shuffled_espresso_consumption)

sorted_french_press_weeks = weeks[np.argsort(shuffled_french_press_consumption)]
sorted_french_press_consumption = np.sort(shuffled_french_press_consumption)

sorted_americano_weeks = weeks[np.argsort(shuffled_americano_consumption)]
sorted_americano_consumption = np.sort(shuffled_americano_consumption)

colors = ['#fdae61', '#2b8cbe', '#d73027']

fig, ax = plt.subplots(3, 1, figsize=(14, 18), sharex=True)

ax[0].bar(sorted_espresso_weeks, sorted_espresso_consumption, color=colors[0], alpha=0.8)
ax[0].set_title("Espresso", fontsize=14, fontweight='bold')
ax[0].set_ylabel("Cups", fontsize=12)

ax[1].bar(sorted_french_press_weeks, sorted_french_press_consumption, color=colors[1], alpha=0.8)
ax[1].set_title("French Press", fontsize=14, fontweight='bold')
ax[1].set_ylabel("Cups", fontsize=12)

ax[2].bar(sorted_americano_weeks, sorted_americano_consumption, color=colors[2], alpha=0.8)
ax[2].set_title("Americano", fontsize=14, fontweight='bold')
ax[2].set_ylabel("Cups", fontsize=12)
ax[2].set_xlabel("Wk", fontsize=12)

for a in ax:
    a.set_xticks(weeks[::4])
    a.set_xticklabels(['Wk {}'.format(i) for i in weeks[::4]], rotation=45)

plt.tight_layout()
plt.show()