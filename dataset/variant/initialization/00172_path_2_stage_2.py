import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(categories, data, title, colors):
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for city_data, color, city_label in zip(data, colors, ['EcoVille', 'Greenburg']):
        values = city_data + city_data[:1]
        ax.fill(angles, values, color=color, alpha=0.25, label=city_label)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, color='gray')
    plt.title(title, size=15, color='darkblue', y=1.1, weight='bold', multialignment='center')
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title='Cities', title_fontsize='13')
    ax.set_ylim(0, 10)
    ax.set_yticklabels([])
    plt.tight_layout()
    plt.show()

categories = ['Air Quality', 'Green Space', 'Waste Management', 
              'Water Management', 'Renewable Energy', 'Public Transportation']
data = [
    [8, 6, 9, 7, 6, 8],   
    [7, 8, 6, 8, 7, 7]    
]
colors = ['#1f77b4', '#ff7f0e']

create_radar_chart(categories, data, 
                   'City Green Index:\nUrban Environmental Performance', 
                   colors)