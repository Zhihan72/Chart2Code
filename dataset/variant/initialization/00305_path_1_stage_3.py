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

changed_colors = ['#e07b39', '#4c72b0', '#55a868', '#64b5cd', '#c44e52', '#8172b2', '#ccb974']
marker_styles = ['o', '^', 's', 'p', '*', 'D', 'x']
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']

fig, ax = plt.subplots(figsize=(14, 10))

ax.plot(years, ai_employment, color=changed_colors[0], linestyle=line_styles[0], marker=marker_styles[0])
ax.plot(years, robotics_employment, color=changed_colors[1], linestyle=line_styles[1], marker=marker_styles[1])
ax.plot(years, vr_employment, color=changed_colors[2], linestyle=line_styles[2], marker=marker_styles[2])
ax.plot(years, blockchain_employment, color=changed_colors[3], linestyle=line_styles[3], marker=marker_styles[3])
ax.plot(years, green_tech_employment, color=changed_colors[4], linestyle=line_styles[4], marker=marker_styles[4])
ax.plot(years, quantum_computing_employment, color=changed_colors[5], linestyle=line_styles[5], marker=marker_styles[5])
ax.plot(years, bioinformatics_employment, color=changed_colors[6], linestyle=line_styles[6], marker=marker_styles[6])

ax.grid(True, linestyle='--', linewidth=0.5)

ax.spines['top'].set_lw(1.5)
ax.spines['right'].set_linestyle(':')
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_linestyle('--')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_ylim(0, 1000)
plt.tight_layout()
plt.show()