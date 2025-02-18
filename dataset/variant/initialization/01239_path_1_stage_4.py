import matplotlib.pyplot as plt

satisfaction_scores = {
    'Computer Science': [8, 7, 9, 6, 8, 7, 9, 10, 9, 5, 7, 6, 8, 9, 7, 9],
    'Humanities': [6, 5, 7, 8, 6, 5, 6, 7, 5, 5, 6, 7, 5, 8, 4, 5],
    'Business': [7, 8, 6, 8, 7, 7, 9, 6, 6, 7, 7, 6, 7, 8, 9, 7],
    'Engineering': [9, 8, 7, 9, 10, 8, 7, 9, 8, 9, 8, 8, 9, 9, 8, 7],
    'Sciences': [7, 8, 7, 8, 7, 8, 6, 7, 7, 8, 8, 9, 7, 8, 6, 7],
    'Arts': [5, 6, 6, 7, 6, 5, 6, 8, 7, 7, 6, 5, 6, 7, 6, 5]
}

data = list(satisfaction_scores.values())
departments = list(satisfaction_scores.keys())

plt.figure(figsize=(12, 9))
box = plt.boxplot(data, notch=False, vert=True, patch_artist=True, labels=departments)

# Apply a single color across all boxes
consistent_color = '#B0E57C'
for patch in box['boxes']:
    patch.set_facecolor(consistent_color)

for median in box['medians']:
    median.set(color='red', linewidth=2)

for whisker in box['whiskers']:
    whisker.set(color='blue', linewidth=1.5)

for cap in box['caps']:
    cap.set(color='blue', linewidth=1.5)

plt.title('Satisfaction in Higher Education', fontsize=16, fontweight='bold')
plt.xlabel('Departments', fontsize=12)
plt.ylabel('Satisfaction Scores (1 to 10)', fontsize=12)
plt.grid(axis='y', linestyle=':', linewidth=0.7, alpha=0.5)

plt.xticks(rotation=15)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()