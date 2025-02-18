import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Butter Pecan', 'Mango']
winter_popularity = [20, 18, 12, 10, 15, 17, 8]
summer_popularity = [10, 15, 22, 8, 10, 9, 26]

# New set of colors; manually defined
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0']

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
season_titles = ["Winter Flavor Favorites", "Summer Flavor Favorites"]
seasonal_popularities = [winter_popularity, summer_popularity]

for i, ax in enumerate(axs):
    wedges, texts, autotexts = ax.pie(seasonal_popularities[i], labels=flavors, colors=new_colors, autopct='%1.0f%%',
                                      startangle=90, pctdistance=0.75, wedgeprops=dict(edgecolor='gray', linestyle='--'),
                                      explode=[0.1 if flavor == 'Mint' else 0 for flavor in flavors])

    centre_circle = plt.Circle((0, 0), 0.60, fc='lightgray', edgecolor='darkgray', linestyle='dotted')
    ax.add_artist(centre_circle)
    
    ax.set_title(season_titles[i], fontsize=14, fontweight='bold', pad=20)

    for text in texts:
        text.set_fontsize(9)
        text.set_fontstyle('italic')
    for autotext in autotexts:
        autotext.set_fontsize(8)
        autotext.set_fontweight('light')
        autotext.set_color('navy')

fig.suptitle('Favorite Ice Cream Flavors in a Small Town Across Selected Seasons', fontsize=16, fontweight='bold', y=1.02)
fig.tight_layout()
plt.show()