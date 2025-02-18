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
colors = ['#1E90FF', '#3CB371', '#FF4500']  # Changed colors
positions = np.arange(len(genres))
bottom = np.zeros(len(genres))

markers = ['o', 'v', '^']  # Added marker styles
hatch_styles = ['', '//', '\\\\']  # Added hatch styles for bars

# Create a stacked bar chart with changes
for idx, (publisher, color, marker, hatch_style) in enumerate(zip(publishers, colors, markers, hatch_styles)):
    ax.bar(positions, data[idx], width=0.6, color=color, label=publisher, bottom=bottom, 
           alpha=0.75, edgecolor='black', hatch=hatch_style)
    bottom += data[idx]

ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Publications Count', fontsize=12)
ax.set_title('Yearly Publications by Publisher', fontsize=16, fontweight='bold')
ax.set_xticks(positions)
ax.set_xticklabels(genres, rotation=30)  # Rotate labels for better readability

ax.legend(title='Publisher', loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)  # Changed legend location

# Added grid
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='gray')

for idx, genre_position in enumerate(positions):
    cumulative_height = 0
    for publisher_data, color in zip(data[:, idx], colors):
        cumulative_height += publisher_data
        ax.text(genre_position, cumulative_height - publisher_data / 2, str(publisher_data),
                ha='center', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()