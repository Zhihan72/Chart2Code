import numpy as np
import matplotlib.pyplot as plt
from math import pi

domains = ['Spellcasting', 'Potion Brewing', 'Herbology', 'Astronomy', 'Alchemy', 'Rune Magic']

arcane_academy = [9, 5, 7, 8, 6, 7]
elderwood_grove = [7, 9, 5, 6, 8, 6]
silver_spire = [8, 7, 6, 9, 7, 5]
shadow_haven = [6, 8, 9, 7, 5, 8]

academies_data = {
    'Arcane Academy': arcane_academy,
    'Elderwood Grove': elderwood_grove,
    'Silver Spire': silver_spire,
    'Shadow Haven': shadow_haven
}

academy_colors = {
    'Arcane Academy': 'blue',
    'Elderwood Grove': 'orange',
    'Silver Spire': 'red',
    'Shadow Haven': 'brown'
}

def create_radar_chart(title, academy_data, labels, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

    academy_data += academy_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='grey', size=10)
    ax.set_rlabel_position(0)
    plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color="grey", size=7)
    plt.ylim(0, 10)

    ax.plot(angles, academy_data, linewidth=2, linestyle='solid')
    ax.fill(angles, academy_data, color=color, alpha=0.4)  # Fill area under radar plot
    plt.title(title, size=16, color=color, y=1.1, weight='bold')

for academy_name, skill_levels in academies_data.items():
    create_radar_chart(f'{academy_name} Mystic Skill Set', skill_levels, domains, academy_colors[academy_name])

plt.tight_layout()
plt.show()