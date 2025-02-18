import numpy as np
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

kids = [3, 4, 3, 4, 4, 5, 6]
teens = [4, 5, 4, 5, 5, 6, 7]
adults = [5, 6, 5, 6, 6, 7, 8]
seniors = [4, 5, 5, 5, 6, 6, 7]

data = np.array([kids, teens, adults, seniors])

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Colors have been shuffled
axs[0].barh(range(len(data)), np.mean(data, axis=1), color=['#98FB98', '#FFDAB9', '#FFB6C1', '#87CEFA'])
axs[0].set_xlim(-10, 10)
axs[0].set_yticks(range(len(data)))
axs[0].set_yticklabels(["Kids", "Teens", "Adults", "Seniors"])
axs[0].invert_yaxis()
axs[0].grid(axis='y', linestyle='-', linewidth=0.7, alpha=0.5)

# Diverging bar chart with shuffled colors
x = np.arange(len(days))
colors = ['#98FB98', '#FFDAB9', '#FFB6C1', '#87CEFA']  # Shuffled colors
bottom = np.zeros(len(days))

for i, category in enumerate(["Kids", "Teens", "Adults", "Seniors"]):
    dataset = data[i]
    axs[1].bar(x, dataset - np.mean(dataset), bottom=bottom, color=colors[i], label=category, hatch='/')
    bottom += (dataset - np.mean(dataset))

axs[1].set_xticks(x)
axs[1].set_xticklabels(days, rotation=30)
axs[1].axhline(0, color='gray', linewidth=1.0)
axs[1].legend(loc='upper left', frameon=True)
axs[1].grid(axis='x', linestyle='-', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()