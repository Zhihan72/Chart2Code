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

new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#42d4f4']

fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

wedges, _, autotexts = ax.pie(
    distribution, colors=new_colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3), shadow=True, explode=(0.05,) * len(genres)
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

ax2 = ax.twinx()

x = np.arange(len(trend_data['Science Fiction']))

for i, genre in enumerate(genres):
    ax2.plot(x, trend_data[genre], marker='o', linestyle='-', color=new_colors[i])

ax2.set_xticks(x)

plt.tight_layout()
plt.show()