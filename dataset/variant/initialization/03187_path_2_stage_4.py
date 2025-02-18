import matplotlib.pyplot as plt
import numpy as np

characters = ['Thorin Ironfist', 'Lyria Swift', 'Elara the Wise', 'Drogon the Mystic']
categories = ['Intelligence', 'Charisma', 'Wisdom', 'Strength', 'Luck', 'Dexterity']
num_categories = len(categories)

elara_attributes = [9, 7, 8, 4, 5, 6]
thorin_attributes = [5, 6, 5, 9, 4, 7]
lyria_attributes = [7, 8, 6, 6, 7, 9]
drogon_attributes = [8, 5, 9, 5, 6, 5]

data = [elara_attributes, thorin_attributes, lyria_attributes, drogon_attributes]
data_with_closure = [d + [d[0]] for d in data]

angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

colors = ['#FF6347', '#32CD32', '#FFD700', '#8A2BE2']
line_styles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D']
alpha_values = [0.3, 0.4, 0.35, 0.5]

for idx, attribute_values in enumerate(data_with_closure):
    ax.fill(angles, attribute_values, color=colors[idx], alpha=alpha_values[idx])
    ax.plot(angles, attribute_values, color=colors[idx], linewidth=2, linestyle=line_styles[idx], marker=markers[idx])

plt.xticks(angles[:-1], categories, color='darkblue', size=12)
plt.title('Hero Abilities Clash in Arcadia:\nA Mythical Chart of Heroes', size=14, color='maroon', pad=20)
plt.legend(characters, loc='lower left', fontsize=10, title='Legendary Figures')
ax.spines['polar'].set_visible(False)
plt.grid(color='grey', linestyle=':', linewidth=0.7)
plt.tight_layout()
plt.show()