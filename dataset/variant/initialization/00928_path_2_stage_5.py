import matplotlib.pyplot as plt
import numpy as np

regions = ['Americas', 'Europe', 'Asia-Pacific', 'Middle East', 'Africa']

consumption_data = np.array([
    [20, 15, -35, 10, -5],  
    [35, -30, -5, 5, 15],  
    [-20, 30, -10, 15, -10] 
])

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
indices = np.arange(len(regions))
bottoms = np.zeros(len(regions))
colors = ['#D2B48C', '#DEB887', '#8B4513', '#A0522D', '#CD853F']

for i in range(consumption_data.shape[0]):
    ax.bar(indices, consumption_data[i, :], bar_width, bottom=bottoms,
           color=colors[i])
    bottoms += consumption_data[i, :]

ax.set_xticks(indices)
ax.set_xticklabels(regions)
ax.axhline(0, color='black', linewidth=0.8)

plt.show()