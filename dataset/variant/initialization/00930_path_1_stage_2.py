import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))

espresso_consumption = 220 + 50 * np.sin(np.linspace(0, 4 * np.pi, 52)) + np.linspace(0, 10, 52)
french_press_consumption = 200 + 45 * np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 8) + np.linspace(5, 15, 52)
americano_consumption = 180 + 40 * np.sin(np.linspace(0, 4 * np.pi, 52) - np.pi / 6) + np.linspace(10, 20, 52)

espresso_errors = 5 + 3 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52)))
french_press_errors = 6 + 4 * np.abs(np.cos(np.linspace(0, 4 * np.pi, 52)))
americano_errors = 7 + 2 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 3))

fig, ax = plt.subplots(3, 1, figsize=(14, 18), sharex=True)

colors = ['#fdae61', '#d73027', '#2b8cbe']

ax[0].errorbar(weeks, espresso_consumption, yerr=espresso_errors, color=colors[0], capsize=3, marker='o', linestyle='-', alpha=0.8)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax[1].errorbar(weeks, french_press_consumption, yerr=french_press_errors, color=colors[1], capsize=3, marker='s', linestyle='--', alpha=0.8)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax[2].errorbar(weeks, americano_consumption, yerr=americano_errors, color=colors[2], capsize=3, marker='^', linestyle='-.', alpha=0.8)
ax[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for a in ax:
    a.set_xticks(weeks[::4])
    a.set_xticklabels([])
    a.set_yticklabels([])

plt.tight_layout()
plt.show()