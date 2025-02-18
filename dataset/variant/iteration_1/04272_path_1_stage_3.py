import matplotlib.pyplot as plt

budgets = [22, 12, 18, 11, 20, 4, 13]

colors = ['#ffd700', '#4682b4', '#20b2aa', '#ff6347', '#6b8e23', '#ba55d3', '#ffa07a']

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(
    budgets,
    colors=colors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=140,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.tight_layout()
plt.show()