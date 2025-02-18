import matplotlib.pyplot as plt

# Updated lists after removing 'Moon' and 'Titan'
destinations = ['Europa', 'Mars', 'Venus', 'Enceladus', 'Asteroid Belt']
budget_allocation = [20, 35, 10, 5, 10]
colors = ['#3498DB', '#FF5733', '#F39C12', '#85C1E9', '#E67E22']
explode = (0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=190,
    wedgeprops=dict(width=0.4)
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')
plt.title("Funding Allocation for Space Missions\n(2035-2045)", fontsize=14, fontweight='bold')

plt.show()