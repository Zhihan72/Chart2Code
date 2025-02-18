import matplotlib.pyplot as plt

age_groups = ['Under 18', '19-35', '36-50', '51 and up']
flavors = ['Vanilla Bean', 'Dark Chocolate', 'Berry', 'Herbal', 'Espresso']

data = {
    '0-18': [20, 30, 30, 15, 5],
    '19-35': [25, 25, 20, 20, 10],
    '36-50': [15, 35, 20, 20, 10],
    '51-70': [25, 25, 20, 10, 20]
}

colors = ['#FFA07A', '#8B4513', '#FF1493', '#98FB98', '#D2691E']

fig, axs = plt.subplots(1, 4, figsize=(16, 6), subplot_kw=dict(aspect='equal'))

for ax, (age, percentages) in zip(axs, data.items()):
    wedges, texts, autotexts = ax.pie(
        percentages, labels=flavors, autopct='%1.1f%%', startangle=140,
        colors=colors, textprops={'fontsize': 9}, wedgeprops={'width': 0.3, 'edgecolor': 'gray'}
    )
    ax.set_title(f'Group {age} Taste', fontsize=12, weight='bold', pad=15)
    for autotext in autotexts:
        autotext.set_color('white')

plt.suptitle('Favorite Ice Cream Flavors By Age Bracket', 
             fontsize=16, weight='bold', y=1.02)

plt.tight_layout()
plt.show()