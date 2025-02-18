import matplotlib.pyplot as plt
import numpy as np

categories = ['Combat', 'Intelligence', 'Leadership', 'Technology', 'Logistics', 'Teamwork']
team_data = {
    'Alpha Squad': [7, 8, 6, 9, 5, 7],
    'Bravo Brigade': [6, 7, 8, 6, 7, 8],
    'Charlie Crew': [9, 6, 7, 8, 6, 7],
    'Delta Division': [8, 7, 6, 7, 9, 6]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for team, values in team_data.items():
    values += values[:1]
    ax.fill(angles, values, alpha=0.25)

ax.set_ylim(0, 10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='darkred')

plt.tight_layout()
plt.show()