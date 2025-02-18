import matplotlib.pyplot as plt
import numpy as np

# Simplified data for fruit preferences
fruit_types = ['Appl', 'Bana', 'Cher', 'Grap', 'Oran']
preferences_percentages = [30, 15, 25, 10, 20]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Pie chart for community fruit preferences
ax[0].pie(
    preferences_percentages, labels=fruit_types, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, explode=(0.1, 0, 0, 0.1, 0), shadow=True
)
centre_circle1 = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle1)
ax[0].axis('equal')
ax[0].set_title('Fruit Pref. Market', fontsize=14, fontweight='bold', pad=20)

# Simplified data for grape preferences
grape_subtypes = ['Red', 'Green', 'Black']
grape_preferences = [25, 15, 60]
grape_colors = ['#ff6666', '#99ff99', '#6666ff']

y_pos = np.arange(len(grape_subtypes))

# Barh chart for grape preferences
ax[1].barh(y_pos, grape_preferences, color=grape_colors, edgecolor='black')
ax[1].set_yticks(y_pos)
ax[1].set_yticklabels(grape_subtypes)
ax[1].invert_yaxis()
ax[1].set_xlabel('%', fontsize=12)

for index, value in enumerate(grape_preferences):
    ax[1].text(value + 2, index, f'{value}%', va='center', ha='left', fontsize=10)

ax[1].set_title('Grape Dist.', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()