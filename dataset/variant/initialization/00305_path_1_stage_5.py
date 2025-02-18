import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

def calculate_growth(base_value, rate, years):
    return base_value * ((1 + rate) ** np.arange(len(years)))

# Altering the base values or growth rates while keeping the original structure
base_ai = 120
base_robotics = 45
base_vr = 35
base_blockchain = 30
base_green_tech = 55
base_quantum_computing = 12
base_bioinformatics = 33

growth_ai = 0.12
growth_robotics = 0.15
growth_vr = 0.14
growth_blockchain = 0.16
growth_green_tech = 0.11
growth_quantum_computing = 0.22
growth_bioinformatics = 0.11

ai_employment = calculate_growth(base_ai, growth_ai, years)
robotics_employment = calculate_growth(base_robotics, growth_robotics, years)
vr_employment = calculate_growth(base_vr, growth_vr, years)
blockchain_employment = calculate_growth(base_blockchain, growth_blockchain, years)
green_tech_employment = calculate_growth(base_green_tech, growth_green_tech, years)
quantum_computing_employment = calculate_growth(base_quantum_computing, growth_quantum_computing, years)
bioinformatics_employment = calculate_growth(base_bioinformatics, growth_bioinformatics, years)

changed_colors = ['#e07b39', '#4c72b0', '#55a868', '#64b5cd', '#c44e52', '#8172b2', '#ccb974']
categories = ['AI', 'Robotics', 'VR', 'Blockchain', 'Green Tech', 'Quantum Computing', 'Bioinformatics']
employment_data = [ai_employment, robotics_employment, vr_employment, blockchain_employment, green_tech_employment, quantum_computing_employment, bioinformatics_employment]

fig, ax = plt.subplots(figsize=(14, 10))

width = 0.1
x = np.arange(len(years))

for i, (data, color, category) in enumerate(zip(employment_data, changed_colors, categories)):
    ax.bar(x + i * width, data, width, label=category, color=color)

ax.set_xticks(x + width * (len(categories) - 1) / 2)
ax.set_xticklabels(years, rotation=45)
ax.set_ylim(0, 1000)
ax.set_ylabel('Employment')

ax.legend()
ax.grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()