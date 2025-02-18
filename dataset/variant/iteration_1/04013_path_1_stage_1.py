import matplotlib.pyplot as plt

age_groups = ['0-18', '19-35', '36-50', '51-70', '71+', '71-80']  # Added '71-80'
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Coffee']
data = {
    '0-18': [25, 35, 25, 10, 5],
    '19-35': [20, 30, 15, 25, 10],
    '36-50': [30, 25, 20, 15, 10],
    '51-70': [35, 20, 15, 15, 15],
    '71+': [40, 20, 15, 10, 15],
    '71-80': [30, 25, 20, 15, 10]  # New data series
}

colors = ['#FFA07A', '#8B4513', '#FF1493', '#98FB98', '#D2691E']
fig, axs = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect='equal'))  # Adjusted subplot size

for ax, (age, percentages) in zip(axs, data.items()):
    wedges, texts, autotexts = ax.pie(
        percentages, labels=flavors, autopct='%1.1f%%', startangle=140,
        colors=colors, textprops={'fontsize': 9}, wedgeprops={'edgecolor': 'gray'}
    )
    ax.set_title(f'Age Group {age}', fontsize=12, weight='bold', pad=15)
    for autotext in autotexts:
        autotext.set_color('white')

plt.suptitle('Distribution of Favorite Ice Cream Flavors Among Different Age Groups', 
             fontsize=16, weight='bold', y=1.02)

fig.legend(wedges, flavors, title="Flavors", loc="center right", bbox_to_anchor=(1.1, 0.5), fontsize=12)

plt.tight_layout()
plt.show()