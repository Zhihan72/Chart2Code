import matplotlib.pyplot as plt
import numpy as np

publishers = ['Publisher A', 'Publisher C', 'Publisher D']
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Historical']

data = np.array([
    [120, 150, 80, 100, 90],     
    [90, 130, 110, 95, 85],      
    [170, 160, 150, 140, 130]    
])

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#1E90FF', '#3CB371', '#FF4500']
positions = np.arange(len(genres))
bottom = np.zeros(len(genres))

# Create a stacked bar chart without textual elements
for idx, (color, hatch_style) in enumerate(zip(colors, ['', '//', '\\\\'])):
    ax.bar(positions, data[idx], width=0.6, color=color, bottom=bottom, 
           alpha=0.75, edgecolor='black', hatch=hatch_style)
    bottom += data[idx]

ax.set_xticks(positions)
ax.set_xticklabels([])  # Remove the genre labels

ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='gray')

plt.tight_layout()
plt.show()