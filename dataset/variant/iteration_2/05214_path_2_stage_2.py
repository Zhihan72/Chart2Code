import matplotlib.pyplot as plt
import numpy as np

categories = ['Combat', 'Intelligence', 'Leadership', 'Technology', 'Logistics', 'Teamwork']
team_data = {
    'Alpha Squad': [7, 8, 6, 9, 5, 7],
    'Bravo Brigade': [6, 7, 8, 6, 7, 8],
    'Charlie Crew': [9, 6, 7, 8, 6, 7],
    'Delta Division': [8, 7, 6, 7, 9, 6],
    'Echo Unit': [5, 8, 7, 6, 8, 9]  # New team with additional made-up data
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for team, values in team_data.items():
    values += values[:1]
    ax.fill(angles, values, alpha=0.25, label=team)

ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=9)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='darkred')

plt.title('Superhero Teams Performance in Meta City', size=15, weight='bold', color='darkred', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)
plt.tight_layout()
plt.show()