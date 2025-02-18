import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2026)

organic_cotton = np.array([
    [15, 30, 5, 10, 20, 25],   
    [8, 20, 12, 24, 16, 4],    
    [11, 35, 17, 29, 23, 6],   
    [14, 23, 28, 9, 18, 5],    
    [19, 3, 23, 15, 11, 7]     
])

recycled_polyester = np.array([
    [8, 12, 19, 3, 15, 5],     
    [21, 18, 14, 4, 7, 11],    
    [17, 22, 2, 13, 6, 9],     
    [16, 20, 5, 13, 3, 9],     
    [18, 14, 6, 10, 22, 4]     
])

hemp = np.array([
    [4, 10, 2, 6, 12, 8],      
    [9, 5, 11, 3, 7, 1],       
    [8, 5, 11, 14, 3, 17],     
    [13, 7, 10, 4, 15, 2],     
    [1, 6, 4, 8, 10, 2]        
])

fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.25
x_indexes = np.arange(len(years))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i in range(5):
    ax.bar(x_indexes + i * bar_width, organic_cotton[i], width=bar_width, color=colors[0], alpha=0.7, label='Organic Cotton' if i == 0 else "")
    ax.bar(x_indexes + i * bar_width + bar_width, recycled_polyester[i], width=bar_width, color=colors[1], alpha=0.7, label='Recycled Polyester' if i == 0 else "")
    ax.bar(x_indexes + i * bar_width + 2 * bar_width, hemp[i], width=bar_width, color=colors[2], alpha=0.7, label='Hemp' if i == 0 else "")

ax.set_xticks(x_indexes + bar_width)
ax.set_xticklabels(years)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(axis='y', linestyle=':', linewidth=0.8, alpha=0.6, color='gray')

plt.legend()
plt.tight_layout(rect=[0, 0, 1, 1])

plt.show()