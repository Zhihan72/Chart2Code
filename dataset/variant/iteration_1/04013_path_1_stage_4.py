import matplotlib.pyplot as plt

age_groups = ['0-18', '19-35', '36-50', '51-70', '71+', '71-80']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Coffee']
data = {
    '0-18': [25, 35, 25, 10, 5],
    '71-80': [30, 25, 20, 15, 10],
    '36-50': [30, 25, 20, 15, 10],
    '51-70': [35, 20, 15, 15, 15],
    '71+': [40, 20, 15, 10, 15],
    '19-35': [20, 30, 15, 25, 10]
}

colors = ['#4682B4', '#EE82EE', '#32CD32', '#DAA520', '#FF6347']
fig, axs = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect='equal'))

for ax, (age, percentages) in zip(axs, data.items()):
    wedges, texts, autotexts = ax.pie(
        percentages, labels=None, autopct='%1.1f%%', startangle=90,
        colors=colors, textprops={'fontsize': 9}, wedgeprops={'edgecolor': 'black', 'linestyle': '--'}
    )
    ax.set_title(f'Age Group {age}', fontsize=14, weight='light', pad=10)
    ax.grid(True, which='major', linestyle=':', color='gray', linewidth=0.75)
    for autotext in autotexts:
        autotext.set_color('black')
    
plt.suptitle('Distribution of Favorite Ice Cream Flavors Among Different Age Groups', 
             fontsize=18, weight='normal', y=1.02)

fig.legend(wedges, flavors, title="Flavors", loc="upper center", bbox_to_anchor=(0.5, 0.1), fontsize=11)

plt.tight_layout()
plt.show()