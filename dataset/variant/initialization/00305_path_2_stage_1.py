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

fig, ax = plt.subplots(figsize=(12, 9))

ax.bar(years, ai_employment, label='AI', color='#ff9999', alpha=0.8, hatch='o')
ax.bar(years, robotics_employment, bottom=ai_employment, label='Robotics', color='#66b3ff', alpha=0.8, hatch='x')
ax.bar(years, vr_employment, bottom=ai_employment+robotics_employment, label='VR', color='#99ff99', alpha=0.8, hatch='/')
ax.bar(years, blockchain_employment, bottom=ai_employment+robotics_employment+vr_employment, label='Blockchain', color='#ffcc99', alpha=0.8, hatch='\\')
ax.bar(years, green_tech_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment, label='Green Tech', color='#c2c2f0', alpha=0.8, hatch='-')
ax.bar(years, quantum_computing_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment, label='Quantum Computing', color='#ffb3e6', alpha=0.8, hatch='*')
ax.bar(years, bioinformatics_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment+quantum_computing_employment, label='Bioinformatics', color='#c9d7e9', alpha=0.8, hatch='|')

ax.set_title('Projected Employment Trends in Future Technologies (2025-2035)', fontsize=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Employment (in thousands)', fontsize=12)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Technology Sectors', fontsize=9, frameon=True, shadow=True)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=60)

ax.set_ylim(0, 1000)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()

plt.show()