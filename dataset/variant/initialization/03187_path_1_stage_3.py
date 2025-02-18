import matplotlib.pyplot as plt
import numpy as np

characters = ['Elara the Wise', 'Thorin Ironfist', 'Lyria Swift', 'Drogon the Mystic']
categories = ['Strength', 'Intelligence', 'Dexterity', 'Charisma', 'Wisdom', 'Luck']
num_categories = len(categories)

elara_attributes = [6, 8, 5, 9, 4, 7]
thorin_attributes = [5, 4, 7, 9, 6, 5]
lyria_attributes = [9, 6, 7, 6, 8, 7]
drogon_attributes = [8, 9, 5, 6, 5, 5]

data = [elara_attributes, thorin_attributes, lyria_attributes, drogon_attributes]
data_with_closure = [d + [d[0]] for d in data]

angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

colors = ['#32CD32', '#FFD700', '#FF6347', '#4682B4']
for i, attribute_values in enumerate(data_with_closure):
    ax.fill(angles, attribute_values, color=colors[i], alpha=0.25, label=characters[i])
    ax.plot(angles, attribute_values, color=colors[i], linewidth=2)

plt.xticks(angles[:-1], categories, color='grey', size=12)
plt.title('Character Attribute Comparison in Fantasia:\nA Radar Chart of Fictional Heroes', size=14, color='navy', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Characters')

plt.tight_layout()
plt.show()