import numpy as np
import matplotlib.pyplot as plt

sectors = ['Solar', 'Wind', 'Hydro', 'Geo', 'Bio']
regions = ['NA', 'EU', 'AS', 'OC', 'AF']

data = {
    'NA': [35, 30, 25, 5, 5],
    'EU': [30, 35, 10, 15, 10],
    'AS': [25, 20, 35, 15, 5],
    'OC': [20, 25, 20, 25, 10],
    'AF': [15, 10, 25, 25, 25]
}

def create_radar_chart(sectors, data, title, region_colors):
    num_vars = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 4)
    ax.set_theta_direction(1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='darkred')

    for idx, (region, values) in enumerate(data.items()):
        values += values[:1]
        ax.fill(angles, values, color=region_colors[idx], alpha=0.25, label=region)

    plt.title(title, size=18, weight='bold', color='darkgreen', va='bottom', pad=30)
    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0.5), fontsize=9, title="Regions", title_fontsize=11)
    ax.yaxis.grid(True, color='blue', linestyle=':', alpha=0.3)
    ax.xaxis.grid(False)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(['10%', '20%', '30%', '40%', '50%'], color='black', size=10)
    plt.tight_layout()
    plt.show()

region_colors = ['#00FF00', '#FF4500', '#FF00FF', '#00FFFF', '#FFD700']
title = "Renewable Energy Trends"
create_radar_chart(sectors, data, title, region_colors)