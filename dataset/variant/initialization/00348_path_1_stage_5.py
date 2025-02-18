import matplotlib.pyplot as plt

destinations = ['Europa', 'Mars', 'Venus', 'Enceladus', 'Asteroid Belt']
budget_allocation = [20, 35, 10, 5, 10]
single_color = '#3498DB'  # Consistent color for all data groups
explode = (0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=[single_color] * len(destinations),  # Applying the color consistently
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