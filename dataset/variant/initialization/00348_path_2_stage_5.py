import matplotlib.pyplot as plt

destinations = ['Europa', 'Venus', 'Titan', 'Ast. Belt', 'Mars', 'Enceladus', 'Moon']
budget_allocation = [20, 10, 15, 10, 35, 5, 5]

# New set of colors for the pie chart
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FF66C4']
explode = (0, 0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,  # Apply the new colors here
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='w')
)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')
plt.title("Budget for\nSpace Missions", fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()