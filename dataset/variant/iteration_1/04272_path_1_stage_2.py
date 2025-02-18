import matplotlib.pyplot as plt

categories = [
    'Research and Development', 
    'Recruitment', 
    'Training', 
    'Resources', 
    'Field Missions', 
    'Miscellaneous',
    'Public Relations'
]
budgets = [22, 12, 18, 11, 20, 4, 13]

# Manually shuffled colors for each category
colors = ['#ffd700', '#4682b4', '#20b2aa', '#ff6347', '#6b8e23', '#ba55d3', '#ffa07a']

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

ax.set_title("Annual Budget Allocation of the Wizards' Guild (2023)", fontsize=15, fontweight='bold', pad=20, color='#4b0082')

ax.legend(wedges, categories, title="Budget Categories", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize='12')

plt.tight_layout()
plt.show()