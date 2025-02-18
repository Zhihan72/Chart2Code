import matplotlib.pyplot as plt

destinations = ['Mars', 'Europa', 'Titan', 'Asteroid Belt', 'Venus', 'Enceladus', 'Moon']
budget_allocation = [35, 20, 15, 10, 10, 5, 5]
colors = ['#FF5733', '#3498DB', '#9B59B6', '#E67E22', '#F39C12', '#85C1E9', '#F7DC6F']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4)
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')
plt.title("Budget Distribution for\nGalactic Exploration Missions (2030-2040)", fontsize=14, fontweight='bold')

plt.show()