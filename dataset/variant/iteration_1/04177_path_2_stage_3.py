import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Butter Pecan']

# Seasonal flavor popularity percentages
winter_popularity = [20, 18, 12, 10, 15, 17]
summer_popularity = [10, 15, 22, 8, 10, 9]
fall_popularity = [18, 17, 15, 14, 10, 11]

colors = plt.cm.tab10(np.linspace(0, 1, len(flavors)))

fig, axs = plt.subplots(1, 3, figsize=(14, 5))  # Change here to a single row of 3 subplots
season_titles = ["Winter Flavor Favorites", "Summer Flavor Favorites", "Fall Flavor Favorites"]
seasonal_popularities = [winter_popularity, summer_popularity, fall_popularity]

for i, ax in enumerate(axs):
    wedges, texts, autotexts = ax.pie(seasonal_popularities[i], labels=flavors, colors=colors, autopct='%1.1f%%',
                                      startangle=140, pctdistance=0.85,
                                      wedgeprops=dict(edgecolor='w', width=0.3))
    
    ax.set_title(season_titles[i], fontsize=14, fontweight='bold', pad=20)
    
    for text in texts:
        text.set_fontsize(10)
    
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
        autotext.set_color('black')

fig.suptitle('Favorite Ice Cream Flavors in a Small Town Across Seasons', fontsize=16, fontweight='bold', y=1.05)

fig.tight_layout()
plt.show()