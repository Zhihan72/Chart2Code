import matplotlib.pyplot as plt
import numpy as np

genres = ['Science Fiction', 'Romance', 'Mystery', 'Fantasy', 'Non-Fiction', 'Historical', 'Thriller']
distribution = [20, 25, 15, 20, 10, 10, 15]  # Added Thriller

years = ['2018', '2019', '2020', '2021', '2022']
trend_data = {
    'Science Fiction': [15, 17, 20, 22, 20],
    'Romance': [22, 23, 25, 24, 25],
    'Mystery': [12, 14, 15, 16, 15],
    'Fantasy': [18, 19, 20, 22, 20],
    'Non-Fiction': [10, 11, 10, 9, 10],
    'Historical': [8, 9, 10, 10, 10],
    'Thriller': [10, 12, 14, 13, 15]  # Added trend data for Thriller
}

single_color = '#2ca02c'

fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    distribution, labels=genres, colors=[single_color] * len(genres),
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3), explode=(0.05,) * len(genres)
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)

ax2 = ax.twinx()

x = np.arange(len(years))

for genre in genres:
    ax2.plot(x, trend_data[genre], marker='o', linestyle='-', color=single_color)

ax2.set_xticks(x)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylim(0, 30)

plt.title("Evolution of Literary Tastes:\nCurrent Distribution and Trends Over Time", 
          fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()

plt.show()