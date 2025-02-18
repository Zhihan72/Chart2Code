import matplotlib.pyplot as plt
import numpy as np

genres = ['Sci-Fi', 'Rom', 'Myst', 'Fant', 'Non-Fic', 'Hist', 'Thrill']
distribution = [20, 25, 15, 20, 10, 10, 15]

years = ['2018', '2019', '2020', '2021', '2022']
trend_data = {
    'Sci-Fi': [15, 17, 20, 22, 20],
    'Rom': [22, 23, 25, 24, 25],
    'Myst': [12, 14, 15, 16, 15],
    'Fant': [18, 19, 20, 22, 20],
    'Non-Fic': [10, 11, 10, 9, 10],
    'Hist': [8, 9, 10, 10, 10],
    'Thrill': [10, 12, 14, 13, 15]
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

plt.title("Book Genres: Distribution & Trends", fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()

plt.show()