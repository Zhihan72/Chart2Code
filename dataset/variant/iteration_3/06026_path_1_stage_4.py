import matplotlib.pyplot as plt

genres = ['Adventure', 'Drama', 'Horror', 'Biography']
popularity = [30, 25, 15, 10]
# Manually shuffled colors
colors = ['#ffcc99', '#66b3ff', '#c2c2f0', '#ff9999']
explode = (0.1, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
                                  explode=explode, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12}, shadow=True)

ax.set_title("The Rising Tides of Literature Genres\n(Recent Years)", fontsize=14, fontweight='bold', pad=20)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.tight_layout()
plt.show()