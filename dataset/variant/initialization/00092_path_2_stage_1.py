import matplotlib.pyplot as plt

practices = ['Recycling', 'Composting', 'Energy-saving', 'Water Conservation', 'Public Transportation']
percentages = [30, 25, 20, 15, 10]
colors = ['#76C7C0', '#FFD700', '#FF6F61', '#6B8E23', '#4682B4']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=practices,
    autopct='%1.1f%%',
    pctdistance=0.75,
    wedgeprops=dict(width=0.3),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)
)

centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_weight('bold')

plt.show()