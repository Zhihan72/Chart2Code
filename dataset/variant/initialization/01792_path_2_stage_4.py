import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Jazz', 'Classic', 'Electro', 'Hip-hop', 'Country']
attendance_data = {
    'Pop': [450, 560, 480, 620, 570, 540, 690, 660, 610, 590, 620, 670],
    'Rock': [510, 600, 580, 710, 750, 680, 720, 800, 770, 810, 760, 840],
    'Jazz': [320, 340, 310, 300, 280, 290, 330, 350, 370, 360, 340, 355],
    'Classic': [270, 290, 250, 260, 240, 230, 275, 285, 295, 305, 280, 290],
    'Electro': [550, 530, 620, 610, 600, 570, 640, 690, 680, 720, 700, 710],
    'Hip-hop': [400, 420, 430, 450, 470, 480, 490, 520, 530, 510, 505, 515],
    'Country': [310, 320, 330, 350, 340, 365, 360, 370, 390, 400, 385, 395]
}

data = [attendance_data[genre] for genre in genres]

fig, ax = plt.subplots(figsize=(12, 6))

colors = ['lightgreen', 'lightblue', 'lightcoral', 'lightyellow', 'lightsalmon', 'lightpink', 'lightgray']
shuffled_colors = [colors[2], colors[0], colors[1], colors[5], colors[3], colors[4], colors[6]]

box = ax.boxplot(data, patch_artist=True, notch=True, vert=True,
                 boxprops=dict(facecolor=shuffled_colors[1], color='blue'),
                 whiskerprops=dict(color='blue', linestyle='-.'),
                 capprops=dict(color='blue', linestyle='--'),
                 medianprops=dict(color='purple'),
                 flierprops=dict(markerfacecolor='orange', marker='^', markersize=8, alpha=0.6))

ax.set_title('Attendance by Genre', fontsize=16, fontweight='bold')
ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('Attendees', fontsize=12)
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, fontsize=11)
ax.yaxis.grid(True, linestyle='-.', which='major', color='black', alpha=0.5)

handles = [plt.Line2D([0], [0], color='purple', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='^', color='w', label='Outliers',
                      markerfacecolor='orange', markersize=8, alpha=0.6)]
ax.legend(handles=handles, loc='upper right', fontsize=11)

plt.tight_layout()
plt.show()