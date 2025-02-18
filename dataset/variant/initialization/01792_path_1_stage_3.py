import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Jazz', 'Classical', 'Electronic']
attendance_data = {
    'Pop': [480, 570, 450, 590, 670, 620, 540, 660, 610, 620, 690, 560],
    'Rock': [750, 580, 810, 760, 800, 510, 720, 710, 840, 770, 600, 680],
    'Jazz': [320, 355, 290, 330, 340, 360, 310, 350, 280, 300, 370, 340],
    'Classical': [240, 305, 250, 290, 270, 285, 260, 230, 295, 275, 280, 290],
    'Electronic': [680, 710, 550, 700, 620, 610, 570, 720, 640, 600, 690, 530]
}

data = [attendance_data[genre] for genre in genres]

# Randomly shuffled color assignments and marker types for demonstration
color_assignments = [
    {'facecolor': 'lightpink', 'color': 'purple'},
    {'facecolor': 'lightcoral', 'color': 'darkred'},
    {'facecolor': 'lightblue', 'color': 'blue'},
    {'facecolor': 'lightyellow', 'color': 'orange'},
    {'facecolor': 'lightgreen', 'color': 'green'}
]

fig, ax = plt.subplots(figsize=(10, 6))

box = ax.boxplot(data, patch_artist=True, notch=True, vert=True)  # Notch added

for patch, color in zip(box['boxes'], color_assignments):
    patch.set_facecolor(color['facecolor'])
    patch.set_edgecolor(color['color'])

for whisker, color in zip(box['whiskers'], color_assignments*2):
    whisker.set_color(color['color'])
    whisker.set_linestyle('--')  # Dashed line style

for cap, color in zip(box['caps'], color_assignments*2):
    cap.set_color(color['color'])

for median, color in zip(box['medians'], color_assignments):
    median.set_color(color['color'])  # Multicolored medians

for flier in box['fliers']:
    flier.set(markerfacecolor='brown', marker='d', markersize=8, alpha=0.6)  # Changed marker type and color

ax.set_title('Concert Attendance Trends by Genre\nin Soundville', fontsize=14, fontweight='bold')
ax.set_xlabel('Music Genre', fontsize=12)
ax.set_ylabel('Number of Attendees', fontsize=12)
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, fontsize=11)

ax.yaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.5)  # Different grid style

handles = [plt.Line2D([0], [0], color=color['color'], lw=2, label=f'{genre} Median') for genre, color in zip(genres, color_assignments)]
handles.append(plt.Line2D([0], [0], marker='d', color='w', label='Outliers',
                          markerfacecolor='brown', markersize=8, alpha=0.6))  # Updated legend

ax.legend(handles=handles, loc='upper right', fontsize=9)  # Moved legend position

plt.tight_layout()
plt.show()