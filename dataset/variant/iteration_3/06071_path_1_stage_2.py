import numpy as np
import matplotlib.pyplot as plt
from math import pi

domains = ['Spellcasting', 'Potion Brewing', 'Herbology', 
           'Astronomy', 'Alchemy', 'Rune Magic']

arcane_academy = [7, 8, 5, 9, 6, 8]
elderwood_grove = [8, 6, 9, 8, 5, 7]
silver_spire = [6, 9, 7, 7, 8, 6]
shadow_haven = [8, 7, 7, 6, 9, 5]

academies_data = {
    'Arcane Academy': arcane_academy,
    'Elderwood Grove': elderwood_grove,
    'Silver Spire': silver_spire,
    'Shadow Haven': shadow_haven
}

academy_colors = {
    'Arcane Academy': 'darkorchid',
    'Elderwood Grove': 'limegreen',
    'Silver Spire': '#C0C0C0',
    'Shadow Haven': 'dimgray'
}

def create_radar_chart(title, academy_data, labels, academy_name, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    academy_data += academy_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='black', size=10, fontweight='bold')
    ax.set_rlabel_position(45)
    plt.yticks([2, 4, 6, 8], ["2", "4", "6", "8"], color="black", size=7,)
    plt.ylim(0, 10)

    ax.plot(angles, academy_data, linewidth=3, linestyle='--', marker='o', label=academy_name, markerfacecolor='white')
    ax.fill(angles, academy_data, color=color, alpha=0.1)

    plt.title(title, size=18, color=color, y=1.1, weight='heavy', style='italic')
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.1), frameon=False)

for academy_name, skill_levels in academies_data.items():
    create_radar_chart(f'{academy_name} Mystic Skills', skill_levels, domains, academy_name, academy_colors[academy_name])

plt.tight_layout()
plt.show()