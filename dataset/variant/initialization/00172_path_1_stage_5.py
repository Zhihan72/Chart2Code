import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(categories, data, title, single_color):
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    city_labels = ['City X', 'Urban Y', 'Metropolis Z', 'Town A']
    color_options = ['#ff6347', '#4682b4', '#32cd32', '#ffa500']
    marker_styles = ['o-', 's-', '^-', 'd-']
    
    for idx, (city_data, city_label) in enumerate(zip(data, city_labels)):
        values = city_data + city_data[:1]
        ax.plot(angles, values, marker_styles[idx % len(marker_styles)], color=color_options[idx % len(color_options)], linewidth=2, label=city_label)
        ax.fill(angles, values, color=color_options[idx % len(color_options)], alpha=0.15)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, color='gray')

    ax.spines['polar'].set_visible(False)
    ax.yaxis.grid(True)
    
    plt.title(title, size=15, color='darkblue', y=1.1, weight='bold', multialignment='center')
    plt.legend(loc='lower right', fontsize=8, title='Urban Areas', title_fontsize='11')
    ax.set_ylim(0, 10)
    ax.set_yticklabels([])
    plt.tight_layout()
    plt.show()

categories = ['Air Quality', 'Green Space', 'Waste Management', 
              'Water Management', 'Renewable Energy', 'Public Transportation']

data = [
    [8, 6, 9, 7, 6, 8],
    [7, 8, 6, 8, 7, 7],
    [9, 7, 8, 9, 9, 9],
    [6, 5, 8, 6, 5, 7]
]

single_color = '#1f77b4'  # Consistent single color for all data groups (unchanged in this instance)

create_radar_chart(categories, data, 
                   'City Green Index:\nUrban Environmental Performance', 
                   single_color)