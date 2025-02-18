import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(categories, data):
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    new_colors = ['#2ca02c', '#d62728']
    
    for city_data, color in zip(data, new_colors):
        values = city_data + city_data[:1]
        ax.fill(angles, values, color=color, alpha=0.25)

    ax.set_xticks(angles[:-1])
    new_categories = ['Waste Management', 'Public Transportation', 
                      'Green Space', 'Renewable Energy', 
                      'Air Quality', 'Water Management']  
    ax.set_xticklabels(new_categories, fontsize=10, color='gray')

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

create_radar_chart(categories, data)