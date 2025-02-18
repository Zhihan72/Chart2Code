import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

def calculate_growth(base_value, rate, years):
    return base_value * ((1 + rate) ** np.arange(len(years)))

base_ai = 100
base_robotics = 50
base_vr = 40
base_blockchain = 25
base_green_tech = 60
base_quantum_computing = 10
base_bioinformatics = 30

growth_ai = 0.10
growth_robotics = 0.12
growth_vr = 0.15
growth_blockchain = 0.18
growth_green_tech = 0.10
growth_quantum_computing = 0.25
growth_bioinformatics = 0.13

ai_employment = calculate_growth(base_ai, growth_ai, years)
robotics_employment = calculate_growth(base_robotics, growth_robotics, years)
vr_employment = calculate_growth(base_vr, growth_vr, years)
blockchain_employment = calculate_growth(base_blockchain, growth_blockchain, years)
green_tech_employment = calculate_growth(base_green_tech, growth_green_tech, years)
quantum_computing_employment = calculate_growth(base_quantum_computing, growth_quantum_computing, years)
bioinformatics_employment = calculate_growth(base_bioinformatics, growth_bioinformatics, years)

# New color mapping
new_colors = ['#55a868', '#4c72b0', '#e07b39', '#64b5cd', '#c44e52', '#8172b2', '#ccb974']

fig, ax = plt.subplots(figsize=(14, 10))
ax.bar(years, ai_employment, label='AI', color=new_colors[0], alpha=0.9)
ax.bar(years, robotics_employment, bottom=ai_employment, label='Robotics', color=new_colors[1], alpha=0.9)
ax.bar(years, vr_employment, bottom=ai_employment+robotics_employment, label='VR', color=new_colors[2], alpha=0.9)
ax.bar(years, blockchain_employment, bottom=ai_employment+robotics_employment+vr_employment, label='Blockchain', color=new_colors[3], alpha=0.9)
ax.bar(years, green_tech_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment, label='Green Tech', color=new_colors[4], alpha=0.9)
ax.bar(years, quantum_computing_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment, label='Quantum Computing', color=new_colors[5], alpha=0.9)
ax.bar(years, bioinformatics_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment+quantum_computing_employment, label='Bioinformatics', color=new_colors[6], alpha=0.9)

ax.set_title('Future Tech Occupation Trends\n(2025-2035) Including Diverse Growth Sectors', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Workers (in thousands)', fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Tech Sectors', fontsize=10, frameon=False)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_ylim(0, 1000)
plt.tight_layout()
plt.show()