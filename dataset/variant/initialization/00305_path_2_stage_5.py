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
base_augmented_reality = 35
base_smart_wearables = 45

growth_ai = 0.10
growth_robotics = 0.12
growth_vr = 0.15
growth_blockchain = 0.18
growth_green_tech = 0.10
growth_quantum_computing = 0.25
growth_bioinformatics = 0.13
growth_augmented_reality = 0.16
growth_smart_wearables = 0.11

ai_employment = calculate_growth(base_ai, growth_ai, years)
robotics_employment = calculate_growth(base_robotics, growth_robotics, years)
vr_employment = calculate_growth(base_vr, growth_vr, years)
blockchain_employment = calculate_growth(base_blockchain, growth_blockchain, years)
green_tech_employment = calculate_growth(base_green_tech, growth_green_tech, years)
quantum_computing_employment = calculate_growth(base_quantum_computing, growth_quantum_computing, years)
bioinformatics_employment = calculate_growth(base_bioinformatics, growth_bioinformatics, years)
augmented_reality_employment = calculate_growth(base_augmented_reality, growth_augmented_reality, years)
smart_wearables_employment = calculate_growth(base_smart_wearables, growth_smart_wearables, years)

n_tech = 9
bar_width = 0.1

fig, ax = plt.subplots(figsize=(14, 9))

indices = np.arange(len(years))

ax.bar(indices, ai_employment, bar_width, color='#e41a1c', alpha=0.8, hatch='o')
ax.bar(indices + bar_width, robotics_employment, bar_width, color='#377eb8', alpha=0.8, hatch='x')
ax.bar(indices + 2 * bar_width, vr_employment, bar_width, color='#4daf4a', alpha=0.8, hatch='/')
ax.bar(indices + 3 * bar_width, blockchain_employment, bar_width, color='#984ea3', alpha=0.8, hatch='\\')
ax.bar(indices + 4 * bar_width, green_tech_employment, bar_width, color='#ff7f00', alpha=0.8, hatch='-')
ax.bar(indices + 5 * bar_width, quantum_computing_employment, bar_width, color='#ffff33', alpha=0.8, hatch='*')
ax.bar(indices + 6 * bar_width, bioinformatics_employment, bar_width, color='#a65628', alpha=0.8, hatch='|')
ax.bar(indices + 7 * bar_width, augmented_reality_employment, bar_width, color='#f781bf', alpha=0.8, hatch='.')
ax.bar(indices + 8 * bar_width, smart_wearables_employment, bar_width, color='#999999', alpha=0.8, hatch='+')

ax.set_xticks(indices + (n_tech / 2) * bar_width)
ax.set_xticklabels(years, rotation=60)

ax.set_ylim(0, 500)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()