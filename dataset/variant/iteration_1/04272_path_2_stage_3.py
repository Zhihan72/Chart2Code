import matplotlib.pyplot as plt

categories = ['Arcane Research', 'Adventurer Hiring', 'Skill Enhancement', 'Resource Acquisition', 'Expedition Costs', 'Various Expenses']
budgets = [25, 15, 20, 10, 25, 5]
# Colors have been shuffled compared to the original order
colors = ['#ff6347', '#20b2aa', '#ffd700', '#6b8e23', '#ba55d3', '#ffa07a']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    budgets,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=140,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=11, weight="bold")

ax.set_title("Magical Financial Overview (2023)", fontsize=15, fontweight='bold', pad=20, color='#4b0082')

plt.tight_layout()
plt.show()