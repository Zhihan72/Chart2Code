import numpy as np
import matplotlib.pyplot as plt
from math import pi

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

def create_radar_chart(academy_data, labels, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

    academy_data += academy_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    ax.plot(angles, academy_data, linewidth=2, linestyle='solid')
    ax.fill(angles, academy_data, color=color, alpha=0.4)
    ax.set_yticklabels([])  # Remove radial labels
    ax.set_xticklabels([])  # Remove angular labels

for academy_name, skill_levels in academies_data.items():
    create_radar_chart(skill_levels, ['']*6, academy_colors[academy_name])

plt.tight_layout()
plt.show()