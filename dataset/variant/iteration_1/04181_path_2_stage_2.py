import numpy as np
import matplotlib.pyplot as plt

sectors = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
regions = ['North America', 'Europe', 'Asia', 'Oceania', 'Africa']

data = {
    'North America': [35, 30, 25, 5, 5],
    'Europe': [30, 35, 10, 15, 10],
    'Asia': [25, 20, 35, 15, 5],
    'Oceania': [20, 25, 20, 25, 10],
    'Africa': [15, 10, 25, 25, 25]
}

def create_radar_chart(sectors, data, title, region_colors):
    num_vars = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 4)  # Changed offset
    ax.set_theta_direction(1)  # Changed direction
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='darkred')  # Changed label color

    for idx, (region, values) in enumerate(data.items()):
        values += values[:1]
        ax.plot(angles, values, linewidth=3, linestyle='dashed', label=region, color=region_colors[idx])  # Changed line properties
        ax.scatter(angles, values, color=region_colors[idx], s=50, marker='D', edgecolors='black')  # Added markers

    plt.title(title, size=18, weight='bold', color='darkgreen', va='bottom', pad=30)  # Changed title properties
    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0.5), fontsize=9, title="Regions", title_fontsize=11)  # Changed legend location and appearance
    ax.yaxis.grid(True, color='blue', linestyle=':', alpha=0.3)  # Changed grid properties
    ax.xaxis.grid(False)  # Removed x-axis grid
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(['10%', '20%', '30%', '40%', '50%'], color='black', size=10)  # Changed tick label style
    plt.tight_layout()
    plt.show()

region_colors = ['#FFD700', '#00FF00', '#00FFFF', '#FF00FF', '#FF4500']
title = "Renewable Energy Adoption Trends Across Global Regions"
create_radar_chart(sectors, data, title, region_colors)