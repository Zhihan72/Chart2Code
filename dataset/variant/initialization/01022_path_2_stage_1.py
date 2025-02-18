import matplotlib.pyplot as plt
import numpy as np

attributes = ['Bravery', 'Strength', 'Wisdom', 'Dexterity', 'Honor']
n_attributes = len(attributes)

# Shuffled data for each knight
lancelot = [10, 9, 9, 8, 7]  # Manually shuffled from [9, 10, 7, 8, 9]
gawain = [9, 10, 7, 8, 7]    # Manually shuffled from [8, 7, 9, 7, 10]
percival = [8, 8, 9, 10, 7]  # Manually shuffled from [10, 8, 8, 9, 7]

# Append the first value to close the radar chart
lancelot += lancelot[:1]
gawain += gawain[:1]
percival += percival[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
knight_names = ['Sir Lancelot', 'Sir Gawain', 'Sir Percival']
knight_data = [lancelot, gawain, percival]

for idx, knight in enumerate(knight_data):
    ax.plot(angles, knight, color=colors[idx], linewidth=2, linestyle='solid', label=knight_names[idx])
    ax.fill(angles, knight, color=colors[idx], alpha=0.25)

ax.set_yticklabels([])  # Cleaner look

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), title='Legendary Knights')
plt.title('Attributes of Legendary Knights in Astoria', size=16, fontweight='bold', pad=20)
plt.tight_layout()  # Prevent overlapping text
plt.show()