import numpy as np
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

kids = [3, 4, 3, 4, 4, 5, 6]
teens = [4, 5, 4, 5, 5, 6, 7]
adults = [5, 6, 5, 6, 6, 7, 8]
seniors = [4, 5, 5, 5, 6, 6, 7]

data = np.array([kids, teens, adults, seniors])

weekly_averages = [np.mean(kids), np.mean(teens), np.mean(adults), np.mean(seniors)]

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plot for weekly averages
axs[0].bar(range(len(weekly_averages)), weekly_averages, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
axs[0].set_ylim(0, 8)
axs[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Plot for daily consumption
bar_width = 0.2
x = np.arange(len(days))

axs[1].bar(x - bar_width*1.5, kids, width=bar_width, color='#FF9999')
axs[1].bar(x - bar_width/2, teens, width=bar_width, color='#66B3FF')
axs[1].bar(x + bar_width/2, adults, width=bar_width, color='#99FF99')
axs[1].bar(x + bar_width*1.5, seniors, width=bar_width, color='#FFCC99')

axs[1].set_xticks([]) # Removed x-tick labels
axs[1].set_yticks([]) # Removed y-tick labels
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()