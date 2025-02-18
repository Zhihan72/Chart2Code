import numpy as np
import matplotlib.pyplot as plt
from math import pi

arcane_academy = [7, 8, 5, 9, 6, 8]
elderwood_grove = [8, 6, 9, 8, 5, 7]
silver_spire = [6, 9, 7, 7, 8, 6]
shadow_haven = [8, 7, 7, 6, 9, 5]

# New made-up academies
mystic_meadow = [7, 7, 7, 8, 8, 6]
dusk_valley = [9, 6, 7, 5, 8, 7]

academies_data = {
    'Arcane Academy': arcane_academy,
    'Elderwood Grove': elderwood_grove,
    'Silver Spire': silver_spire,
    'Shadow Haven': shadow_haven,
    'Mystic Meadow': mystic_meadow,
    'Dusk Valley': dusk_valley
}

consistent_color = 'cornflowerblue'

def create_radar_chart(academy_data, color):
    num_vars = len(academy_data)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    academy_data += academy_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_rlabel_position(45)
    plt.ylim(0, 10)

    ax.plot(angles, academy_data, linewidth=3, linestyle='--', marker='o', markerfacecolor='white')
    ax.fill(angles, academy_data, color=color, alpha=0.1)

    ax.tick_params(labelbottom=False, labelleft=False)

for academy_name, skill_levels in academies_data.items():
    create_radar_chart(skill_levels, consistent_color)

plt.tight_layout()
plt.show()