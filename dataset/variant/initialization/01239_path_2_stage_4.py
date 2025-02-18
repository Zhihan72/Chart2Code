import matplotlib.pyplot as plt

satisfaction_scores = {
    'Computer Science': [8, 7, 9, 6, 8, 7, 9, 10, 9, 5, 7, 6, 8, 9, 7, 9],
    'Business': [7, 8, 6, 8, 7, 7, 9, 6, 6, 7, 7, 6, 7, 8, 9, 7],
    'Engineering': [9, 8, 7, 9, 10, 8, 7, 9, 8, 9, 8, 8, 9, 9, 8, 7],
    'Sciences': [7, 8, 7, 8, 7, 8, 6, 7, 7, 8, 8, 9, 7, 8, 6, 7]
}

data = list(satisfaction_scores.values())

plt.figure(figsize=(10, 6))
box = plt.boxplot(data, notch=False, vert=False, patch_artist=True)

new_colors = ['#FF5733', '#33D4FF', '#FF33B5', '#FFC733']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)

plt.grid(axis='x', linestyle=':', linewidth=0.5, alpha=0.8)

for whisker in box['whiskers']:
    whisker.set(color='blue', linewidth=1)

for cap in box['caps']:
    cap.set(color='orange', linewidth=1)

for median in box['medians']:
    median.set(color='red', linewidth=1.5)

plt.tight_layout()
plt.show()