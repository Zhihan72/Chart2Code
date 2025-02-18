import matplotlib.pyplot as plt

age_groups = ['0-18', '19-35', '36-50', '51-70', '71+', '71-80']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Coffee']
data = {
    '0-18': [25, 35, 25, 10, 5],
    '71-80': [30, 25, 20, 15, 10],  # Moved '71-80' here
    '36-50': [30, 25, 20, 15, 10],
    '51-70': [35, 20, 15, 15, 15],
    '71+': [40, 20, 15, 10, 15],
    '19-35': [20, 30, 15, 25, 10]   # Moved '19-35' here
}

# New set of colors for the flavors
colors = ['#FF6347', '#4682B4', '#EE82EE', '#32CD32', '#DAA520']
fig, axs = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect='equal'))

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