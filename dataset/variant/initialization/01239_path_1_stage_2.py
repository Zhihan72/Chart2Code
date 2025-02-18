import matplotlib.pyplot as plt

# Satisfaction scores (1 to 10 scale) for each department, along with an additional department
satisfaction_scores = {
    'Computer Science': [8, 7, 9, 6, 8, 7, 9, 10, 9, 5, 7, 6, 8, 9, 7, 9],
    'Humanities': [6, 5, 7, 8, 6, 5, 6, 7, 5, 5, 6, 7, 5, 8, 4, 5],
    'Business': [7, 8, 6, 8, 7, 7, 9, 6, 6, 7, 7, 6, 7, 8, 9, 7],
    'Engineering': [9, 8, 7, 9, 10, 8, 7, 9, 8, 9, 8, 8, 9, 9, 8, 7],
    'Sciences': [7, 8, 7, 8, 7, 8, 6, 7, 7, 8, 8, 9, 7, 8, 6, 7],
    # New department added with arbitrary data
    'Arts': [5, 6, 6, 7, 6, 5, 6, 8, 7, 7, 6, 5, 6, 7, 6, 5]
}

data = list(satisfaction_scores.values())
departments = list(satisfaction_scores.keys())

plt.figure(figsize=(12, 9))
box = plt.boxplot(data, notch=True, vert=False, patch_artist=True, labels=departments)

colors = ['#FFDDC1', '#FFD1DC', '#C1E1FF', '#C1FFD7', '#FFE4C1', '#E1FFC1']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Student Satisfaction with Online Learning Platforms\nin Higher Education', fontsize=16, fontweight='bold')
plt.xlabel('Satisfaction Scores (1 to 10)', fontsize=12)
plt.ylabel('Departments', fontsize=12)
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

for whisker in box['whiskers']:
    whisker.set(color='grey', linewidth=1.5)

for cap in box['caps']:
    cap.set(color='grey', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

plt.tight_layout()
plt.show()