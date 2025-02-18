import numpy as np
import matplotlib.pyplot as plt

sectors = ['Wind Power', 'Geothermal', 'Hydropower', 'Biomass', 'Solar Power']
regions = ['Europe', 'Asia', 'North America', 'Oceania', 'Africa']

data = {
    'Europe': [20, 35, 30, 10, 5],
    'Asia': [25, 30, 10, 5, 30],
    'North America': [25, 40, 5, 10, 20],
    'Oceania': [30, 10, 25, 15, 20],
    'Africa': [15, 25, 30, 10, 20]
}

def create_radar_chart(sectors, data, title):
    num_vars = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='purple')  # Changed color

    # Altered styles of plot lines and markers
    line_styles = ['solid', 'dashed', 'dashdot', 'dotted']  # Randomly chosen different styles
    
    for idx, (region, values) in enumerate(data.items()):
        values += values[:1]
        linestyle = line_styles[idx % len(line_styles)]  # Different line styles
        marker = 'o' if idx % 2 == 0 else 's'  # Alternate marker shapes
        ax.plot(angles, values, linewidth=2, linestyle=linestyle, marker=marker, label=region)
        ax.fill(angles, values, alpha=0.2) 

    plt.title(title, size=16, weight='bold', color='darkgreen', va='bottom', pad=20)  # Changed title color
    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.2), fontsize=11, title="Region")  # Slightly moved position

    ax.yaxis.grid(True, color='black', linestyle='-', alpha=0.3)  # Changed grid color and style for y-axis
    ax.xaxis.grid(True, color='black', linestyle='-', alpha=0.3)  # Changed grid color and style for x-axis
    ax.set_yticks([10, 20, 30, 40])
    ax.set_yticklabels(['10%', '20%', '30%', '40%'], color='black', size=11)  # Removed one tick and changed colors

    ax.spines['polar'].set_visible(True)  # Made border visible with default style

    plt.tight_layout()
    plt.show()

create_radar_chart(sectors, data, "Global Renewable Trends by Region")