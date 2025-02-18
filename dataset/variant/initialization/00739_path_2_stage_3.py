import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [7, 9, 6, 5, 8],
    [8, 6, 5, 9, 7],
    [5, 8, 6, 7, 7],
    [9, 6, 8, 5, 6],
    [8, 5, 7, 9, 9]   
])

num_vars = data.shape[1]

def create_radar_chart(data):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data = np.concatenate((data, data[:, [0]]), axis=1)
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']
    for d, color in zip(data, colors):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['polar'].set_visible(False)
    ax.set_frame_on(False)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    plt.tight_layout()
    plt.show()

create_radar_chart(data)