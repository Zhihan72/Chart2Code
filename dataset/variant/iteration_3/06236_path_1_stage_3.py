import numpy as np
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

kids = [3, 4, 3, 4, 4, 5, 6]
teens = [4, 5, 4, 5, 5, 6, 7]
adults = [5, 6, 5, 6, 6, 7, 8]
seniors = [4, 5, 5, 5, 6, 6, 7]

data = np.array([kids, teens, adults, seniors])

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plot for weekly averages
axs[0].barh(range(len(data)), np.mean(data, axis=1), color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
axs[0].set_xlim(-8, 8)
axs[0].set_yticks(range(len(data)))
axs[0].set_yticklabels(["Kids", "Teens", "Adults", "Seniors"])
axs[0].invert_yaxis()  # To have the same order as the data list
axs[0].grid(axis='x', linestyle='--', linewidth=0.5, alpha=0.7)

# Diverging bar chart for daily consumption
x = np.arange(len(days))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
bottom = np.zeros(len(days))

for i, category in enumerate(["Kids", "Teens", "Adults", "Seniors"]):
    dataset = data[i]
    axs[1].bar(x, dataset - np.mean(dataset), bottom=bottom, color=colors[i], label=category)
    bottom += (dataset - np.mean(dataset))

axs[1].set_xticks(x)
axs[1].set_xticklabels(days, rotation=45)
axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].legend(loc='best')

plt.tight_layout()
plt.show()