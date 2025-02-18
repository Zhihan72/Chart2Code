import matplotlib.pyplot as plt
import numpy as np

publishers = ['Pub A', 'Pub B', 'Pub C', 'Pub D']
genres = ['Fiction', 'NonFiction', 'SciFi', 'Fantasy', 'History']

data = np.array([
    [120, 150, 80, 100, 90],     
    [200, 180, 170, 160, 140],   
    [90, 130, 110, 95, 85],      
    [170, 160, 150, 140, 130]    
])
num_publishers = data.shape[0]

years = ['Yr 1', 'Yr 2', 'Yr 3', 'Yr 4', 'Yr 5']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
positions = np.arange(len(genres))
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    bar_positions = positions + idx * bar_width
    ax.bar(bar_positions, data[idx], width=bar_width, color=color, alpha=0.75)

ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Publications', fontsize=12)
ax.set_title('Publications by Genres', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width * (num_publishers - 1) / 2)
ax.set_xticklabels(genres)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()