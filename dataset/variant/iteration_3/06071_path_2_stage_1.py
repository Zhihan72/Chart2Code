import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the mystical domains
domains = [
    'Spellcasting', 'Potion Brewing', 'Herbology', 
    'Astronomy', 'Alchemy', 'Rune Magic'
]

# Define the skill levels for each academy
arcane_academy = [7, 8, 5, 9, 6, 8]
elderwood_grove = [8, 6, 9, 8, 5, 7]
silver_spire = [6, 9, 7, 7, 8, 6]
shadow_haven = [8, 7, 7, 6, 9, 5]

# Combine data into a dictionary for easy plotting
academies_data = {
    'Arcane Academy': arcane_academy,
    'Elderwood Grove': elderwood_grove,
    'Silver Spire': silver_spire,
    'Shadow Haven': shadow_haven
}

# New color scheme for each academy
academy_colors = {
    'Arcane Academy': 'blue',
    'Elderwood Grove': 'orange',
    'Silver Spire': 'red',
    'Shadow Haven': 'brown'
}

# Create a radar chart function
def create_radar_chart(title, academy_data, labels, academy_name, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

    academy_data += academy_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='grey', size=10)
    ax.set_rlabel_position(0)
    plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color="grey", size=7)
    plt.ylim(0, 10)

    ax.plot(angles, academy_data, linewidth=2, linestyle='solid', label=academy_name)
    ax.fill(angles, academy_data, color=color, alpha=0.3)
    plt.title(title, size=16, color=color, y=1.1, weight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Plot for each academy
for academy_name, skill_levels in academies_data.items():
    create_radar_chart(f'{academy_name} Mystic Skill Set', skill_levels, domains, academy_name, academy_colors[academy_name])

plt.tight_layout()
plt.show()