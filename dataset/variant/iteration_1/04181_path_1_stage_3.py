import numpy as np
import matplotlib.pyplot as plt

# Manually altered textual elements
sectors = ['Wind Power', 'Geothermal', 'Hydropower', 'Biomass', 'Solar Power']
regions = ['Europe', 'Asia', 'North America', 'Oceania', 'Africa']

data = {
    'Europe': [20, 35, 30, 10, 5],
    'Asia': [25, 30, 10, 5, 30],
    'North America': [25, 40, 5, 10, 20],
    'Oceania': [30, 10, 25, 15, 20],
    'Africa': [15, 25, 30, 10, 20]
}

data_array = np.array([data[region] for region in regions])

def create_radar_chart(sectors, data, title, color):
    num_vars = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='darkblue')

    for region, values in data.items():
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=color)
        ax.fill(angles, values, color=color, alpha=0.25)

    plt.title("Global Renewable Trends by Region", size=16, weight='bold', color='navy', va='bottom', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10, title="Area", title_fontsize=12)

    ax.yaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.xaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(['10%', '20%', '30%', '40%', '50%'], color='gray', size=12)

    ax.spines['polar'].set_visible(False)

    plt.tight_layout()
    plt.show()

color = '#1f77b4'
create_radar_chart(sectors, data, "Global Renewable Trends by Region", color)