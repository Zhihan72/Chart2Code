import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
cuisine1_popularity = [80, 70, 90, 80, 70]  
cuisine2_popularity = [65, 75, 85, 75, 65]  
cuisine3_popularity = [70, 60, 95, 85, 80]  

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.25
x_labels = np.arange(len(regions))

# Apply a single color consistently across all data groups
single_color = 'darkblue'
ax.bar(x_labels - bar_width, cuisine1_popularity, width=bar_width, color=single_color, edgecolor='black', alpha=0.6, label='Cuisine 1', linestyle='-.')
ax.bar(x_labels, cuisine2_popularity, width=bar_width, color=single_color, edgecolor='black', alpha=0.6, label='Cuisine 2', linestyle='-.')
ax.bar(x_labels + bar_width, cuisine3_popularity, width=bar_width, color=single_color, edgecolor='black', alpha=0.6, label='Cuisine 3', linestyle='-.')

ax.grid(axis='y', linestyle='-.', alpha=0.4)
ax.yaxis.set_ticks(np.arange(0, 101, 20))

ax.set_xlabel('Regions')
ax.set_ylabel('Popularity Scores')
ax.set_title('Cuisine Popularity by Region')
ax.set_xticks(x_labels)
ax.set_xticklabels(regions)
ax.legend()

plt.tight_layout()
plt.show()