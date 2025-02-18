import matplotlib.pyplot as plt

# Altered celestial bodies and their budget allocations
destinations = ['Europa', 'Venus', 'Titan', 'Asteroid Belt', 'Mars', 'Enceladus', 'Moon']
budget_allocation = [20, 10, 15, 10, 35, 5, 5]

# Colors inspired by celestial body characteristics
colors = ['#3498DB', '#F39C12', '#9B59B6', '#E67E22', '#FF5733', '#85C1E9', '#F7DC6F']

# Explode the largest slice (Mars) to highlight it
explode = (0, 0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')
plt.title("Budget Distribution for\nGalactic Exploration Missions (2030-2040)", fontsize=14, fontweight='bold')

legend_labels = [f"{destination}: {allocation}%" for destination, allocation in zip(destinations, budget_allocation)]
ax.legend(legend_labels, title="Mission Budget Allocation", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

plt.tight_layout()
plt.show()