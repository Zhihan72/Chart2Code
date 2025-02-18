import matplotlib.pyplot as plt

flavors = ['Apple', 'Banana', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']
preferences = [300, 200, 150, 100, 150, 100]
colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Explode the slice with the highest preference 'Apple'
explode = [0.1 if i == max(preferences) else 0 for i in preferences]

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(
    preferences, explode=explode, labels=flavors, colors=colors, autopct='%1.1f%%', shadow=True, 
    startangle=140, textprops={'fontsize': 9, 'color': 'black'}
)

ax.set_title('Survey of Preferred Fruit Flavors\nAmong Local Residents', fontsize=14, fontweight='bold', pad=20)
ax.legend(wedges, flavors, title="Flavors", loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()