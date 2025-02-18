import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))

espresso_consumption = 220 + 50 * np.sin(np.linspace(0, 4 * np.pi, 52)) + np.linspace(0, 10, 52)
americano_consumption = 180 + 40 * np.sin(np.linspace(0, 4 * np.pi, 52) - np.pi / 6) + np.linspace(10, 20, 52)

espresso_errors = 5 + 3 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52)))
americano_errors = 7 + 2 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 3))

fig, ax = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

colors = ['#fdae61', '#2b8cbe']

ax[0].errorbar(weeks, espresso_consumption, yerr=espresso_errors, color=colors[0], capsize=3, marker='o', linestyle='-', alpha=0.8)
ax[1].errorbar(weeks, americano_consumption, yerr=americano_errors, color=colors[1], capsize=3, marker='^', linestyle='-.', alpha=0.8)

for a in ax:
    a.set_xticks([])
    a.set_yticks([])

plt.tight_layout()
plt.show()