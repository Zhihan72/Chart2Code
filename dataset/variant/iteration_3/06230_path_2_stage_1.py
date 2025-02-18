import matplotlib.pyplot as plt
import numpy as np

flavors = ['Apple', 'Banana', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']
preferences = [300, 200, 150, 100, 150, 100]

colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

explode = [0.1 if i == max(preferences) else 0 for i in preferences]

wedges, texts, autotexts = ax.pie(
    preferences, explode=explode, labels=flavors, colors=colors, autopct='%1.1f%%', 
    startangle=100, pctdistance=0.80, textprops={'fontsize': 10, 'color': 'purple'},
    wedgeprops={'linestyle': '--', 'linewidth': 1.5, 'edgecolor': 'grey'}
)

centre_circle = plt.Circle((0, 0), 0.65, fc='lightgrey')
ax.add_artist(centre_circle)

ax.set_title('Fruit Flavors Survey\nAmong Locals', fontsize=16, fontweight='bold', pad=15)

ax.legend(wedges, flavors, title="Flavors", loc="upper right", bbox_to_anchor=(0.9, 0.9))

plt.grid()
plt.tight_layout()

plt.show()