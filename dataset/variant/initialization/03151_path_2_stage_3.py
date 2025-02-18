import matplotlib.pyplot as plt
import numpy as np

def radar_chart_angles(n):
    return np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()

def create_radar_data(values, angles):
    return values + values[:1], angles + angles[:1]

categories = ['Memory', 'Attention', 'Problem Solving', 'Creativity', 'Verbal Skills',
              'Logical Reasoning', 'Processing Speed', 'Emotional Intelligence']

alpha_mix = [8, 7, 6, 5, 9, 8, 6, 7]
beta_boost = [6, 8, 7, 4, 6, 9, 5, 8]
gamma_grow = [7, 6, 8, 9, 5, 7, 8, 6]
delta_develop = [5, 6, 7, 8, 9, 6, 7, 5]
epsilon_enhance = [9, 5, 6, 7, 8, 9, 6, 8]
zeta_zoom = [7, 8, 8, 6, 7, 8, 7, 6]
eta_elevate = [6, 7, 9, 5, 8, 7, 9, 7]

angles = radar_chart_angles(len(categories))

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.suptitle("Enhanced Cognitive Abilities Through Nutrient Blends", fontsize=14, fontweight='bold', va='bottom')

blends_data = {
    'AlphaMix': alpha_mix, 'BetaBoost': beta_boost, 'GammaGrow': gamma_grow,
    'DeltaDevelop': delta_develop, 'EpsilonEnhance': epsilon_enhance,
    'ZetaZoom': zeta_zoom, 'EtaElevate': eta_elevate
}

single_color = '#4682B4'

for idx, (blend_name, blend_values) in enumerate(blends_data.items()):
    values, angles_filled = create_radar_data(blend_values, angles)
    ax.plot(angles_filled, values, color=single_color, linewidth=2, label=blend_name)

ax.set_yticks(range(1, 11))
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=10)

ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_ylim(0, 10)

plt.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), title="Nutrient Blends", fontsize=10)

plt.tight_layout(rect=[0, 0, 0.95, 1])
plt.show()