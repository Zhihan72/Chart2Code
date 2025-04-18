import numpy as np
import matplotlib.pyplot as plt

sectors = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
regions = ['North America', 'Europe', 'Asia', 'Oceania', 'Africa']

# Manually shuffled and altered scores to give appearance of randomness
data = {
    'North America': [35, 30, 25, 5, 5],
    'Europe': [30, 35, 10, 15, 10],
    'Asia': [25, 20, 35, 15, 5],
    'Oceania': [20, 25, 20, 25, 10],
    'Africa': [15, 10, 25, 25, 25]
}

data_array = np.array([data[region] for region in regions])

def create_radar_chart(sectors, data, title, region_colors):
    num_vars = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='darkblue')

    for idx, (region, values) in enumerate(data.items()):
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=region_colors[idx])
        ax.fill(angles, values, color=region_colors[idx], alpha=0.25)

    plt.title(title, size=16, weight='bold', color='navy', va='bottom', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10, title="Regions", title_fontsize=12)
    ax.yaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.xaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(['10%', '20%', '30%', '40%', '50%'], color='gray', size=12)
    ax.spines['polar'].set_visible(False)
    plt.tight_layout()
    plt.show()

region_colors = ['#FFD700', '#00FF00', '#00FFFF', '#FF00FF', '#FF4500']
title = "Renewable Energy Adoption Trends Across Global Regions"
create_radar_chart(sectors, data, title, region_colors)