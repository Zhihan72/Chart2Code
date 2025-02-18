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

color_assignments = [
    {'facecolor': 'lightpink', 'color': 'purple'},
    {'facecolor': 'lightcoral', 'color': 'darkred'},
    {'facecolor': 'lightblue', 'color': 'blue'},
    {'facecolor': 'lightyellow', 'color': 'orange'},
    {'facecolor': 'lightgreen', 'color': 'green'}
]

fig, ax = plt.subplots(figsize=(10, 6))

box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, labels=genres)

for patch, color in zip(box['boxes'], color_assignments):
    patch.set_facecolor(color['facecolor'])
    patch.set_edgecolor(color['color'])

for whisker, color in zip(box['whiskers'], color_assignments*2):
    whisker.set_color(color['color'])
    whisker.set_linestyle('--')

for cap, color in zip(box['caps'], color_assignments*2):
    cap.set_color(color['color'])

for median, color in zip(box['medians'], color_assignments):
    median.set_color(color['color'])

for flier in box['fliers']:
    flier.set(markerfacecolor='brown', marker='d', markersize=8, alpha=0.6)

ax.xaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.5)

plt.tight_layout()
plt.show()