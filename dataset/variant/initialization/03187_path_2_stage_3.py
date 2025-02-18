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

single_color = '#4682B4'
for attribute_values in data_with_closure:
    ax.fill(angles, attribute_values, color=single_color, alpha=0.25)  # Fill area
    ax.plot(angles, attribute_values, color=single_color, linewidth=2)

plt.xticks(angles[:-1], categories, color='grey', size=12)
plt.title('Hero Abilities Clash in Arcadia:\nA Mythical Chart of Heroes', size=14, color='navy', pad=20)
plt.legend(characters, loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Legendary Figures')
plt.tight_layout()
plt.show()