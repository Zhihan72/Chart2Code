import matplotlib.pyplot as plt

budgets = [22, 12, 18, 11, 20, 4, 13]

colors = ['#ffd700', '#4682b4', '#20b2aa', '#ff6347', '#6b8e23', '#ba55d3', '#ffa07a']

fig, ax = plt.subplots(figsize=(10, 7))

# Plot a standard pie chart without a central circle
ax.pie(
    budgets,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Ensure that the pie chart is circular
ax.axis('equal')

plt.tight_layout()
plt.show()