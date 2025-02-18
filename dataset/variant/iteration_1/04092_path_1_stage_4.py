import matplotlib.pyplot as plt

cities = ['NY', 'Tokyo', 'Berlin', 'Paris', 'Sydney', 'London', 'Cairo', 'Mumbai', 'SP', 'Beijing']
coffee_consumption = [300, 250, 220, 240, 200, 280, 220, 160, 180, 210]

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#FF5733'
bars = ax.bar(cities, coffee_consumption, color=single_color)

for bar, consumption in zip(bars, coffee_consumption):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{consumption}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title('Coffee Consumption by City', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Cities', fontsize=12, labelpad=10)
ax.set_ylabel('Cups/Month', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

plt.tight_layout()
plt.show()