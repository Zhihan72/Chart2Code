import matplotlib.pyplot as plt
import numpy as np

categories = ['Luck', 'Strength', 'Wisdom', 'Charisma', 'Dexterity', 'Intelligence']
num_categories = len(categories)

elara_attributes = [6, 8, 4, 9, 5, 7]
thorin_attributes = [5, 5, 6, 9, 7, 4]
lyria_attributes = [7, 9, 8, 6, 7, 6]
drogon_attributes = [5, 8, 5, 6, 5, 9]

data = [lyria_attributes, drogon_attributes, thorin_attributes, elara_attributes]
data_with_closure = [d + [d[0]] for d in data]

angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32']
for i, attribute_values in enumerate(data_with_closure):
    ax.fill(angles, attribute_values, color=colors[i], alpha=0.25)
    ax.plot(angles, attribute_values, color=colors[i], linewidth=2)

plt.xticks(angles[:-1], categories, color='black', size=12)
plt.title('Fictional Heroes of Fantasia:\nRole Attribute Disparity', size=14, color='navy', pad=20)

plt.tight_layout()
plt.show()