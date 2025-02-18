import matplotlib.pyplot as plt
import numpy as np

genres = ['Science Fiction', 'Romance', 'Mystery', 'Fantasy', 'Non-Fiction', 'Historical', 'Biography']
distribution = [18, 22, 13, 18, 8, 8, 13]

trend_data = {
    'Science Fiction': [15, 17, 20, 22, 20],
    'Romance': [22, 23, 25, 24, 25],
    'Mystery': [12, 14, 15, 16, 15],
    'Fantasy': [18, 19, 20, 22, 20],
    'Non-Fiction': [10, 11, 10, 9, 10],
    'Historical': [8, 9, 10, 10, 10],
    'Biography': [10, 12, 10, 13, 13]
}

# New set of shuffled colors for the pie chart
new_colors = ['#4363d8', '#f58231', '#911eb4', '#42d4f4', '#e6194b', '#ffe119', '#3cb44b']

fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

# Modified wedgeprops and explode for stylistic change
wedges, _, autotexts = ax.pie(
    distribution, colors=new_colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.75, # Changed angles and pctdistance
    wedgeprops=dict(width=0.25, edgecolor='w'), shadow=False, explode=(0.1, 0, 0.05, 0.1, 0, 0.05, 0)
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(9)

ax2 = ax.twinx()

x = np.arange(len(trend_data['Science Fiction']))

# Randomly changed marker types and line styles
markers = ['x', 's', '^', 'D', 'v', '+', '*']
linestyles = ['-', '--', ':', '-.', '-', '--', '-']

for i, genre in enumerate(genres):
    ax2.plot(x, trend_data[genre], marker=markers[i], linestyle=linestyles[i], color=new_colors[i])

ax2.set_xticks(x)
ax2.grid(True, linestyle='--', alpha=0.6) # Added grid lines

plt.tight_layout()
plt.show()