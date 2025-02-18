import matplotlib.pyplot as plt

flavors = ['Choc', 'Van', 'Strawb', 'Mint Choc', 'Cookie D']
popularity = [25, 20, 15, 10, 10]

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFB6C1']
explode = (0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="black"),
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

plt.setp(autotexts, size=10, weight="bold")

ax.set_title(
    "Ice Cream Preferences in Sweetvale", 
    fontsize=14, fontweight='bold', pad=15
)
ax.legend(
    wedges, flavors, title="Flavors", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()

plt.show()