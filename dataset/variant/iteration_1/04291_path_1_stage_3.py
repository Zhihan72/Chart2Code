import matplotlib.pyplot as plt

# Data: Scores for four classes over four exams
class_a_scores = [
    [78, 82, 85, 83, 80, 75, 77, 85, 88, 82],
    [83, 85, 75, 79, 77, 81, 80, 85, 86, 78],
    [88, 85, 83, 87, 80, 79, 85, 89, 86, 84],
    [82, 83, 79, 77, 81, 85, 82, 80, 86, 84]
]

class_b_scores = [
    [65, 70, 68, 72, 69, 67, 66, 71, 74, 69],
    [70, 75, 72, 74, 70, 68, 73, 72, 71, 70],
    [72, 74, 70, 78, 75, 72, 74, 77, 75, 76],
    [68, 72, 74, 73, 70, 68, 71, 75, 77, 74]
]

class_c_scores = [
    [90, 92, 85, 88, 89, 85, 91, 87, 94, 90],
    [88, 87, 85, 89, 92, 91, 90, 93, 87, 88],
    [87, 85, 80, 85, 87, 90, 89, 91, 88, 87],
    [89, 91, 88, 85, 87, 86, 90, 88, 91, 89]
]

class_d_scores = [
    [55, 60, 58, 62, 59, 57, 56, 61, 64, 59],
    [60, 65, 62, 64, 60, 58, 63, 62, 61, 60],
    [62, 64, 60, 68, 65, 62, 64, 67, 65, 66],
    [58, 62, 64, 63, 60, 58, 61, 65, 67, 64]
]

data = class_a_scores + class_b_scores + class_c_scores + class_d_scores
classes = ['Class A Exam 1', 'Class A Exam 2', 'Class A Exam 3', 'Class A Exam 4',
           'Class B Exam 1', 'Class B Exam 2', 'Class B Exam 3', 'Class B Exam 4',
           'Class C Exam 1', 'Class C Exam 2', 'Class C Exam 3', 'Class C Exam 4',
           'Class D Exam 1', 'Class D Exam 2', 'Class D Exam 3', 'Class D Exam 4']

fig, ax = plt.subplots(figsize=(16, 11))

bplots = ax.boxplot(data, vert=False, patch_artist=True, notch=False,
                    boxprops=dict(facecolor='lightyellow', color='blue', linewidth=1.5),
                    whiskerprops=dict(color='blue', linewidth=1.5),
                    capprops=dict(color='blue', linewidth=1.5),
                    medianprops=dict(color='red', linewidth=1.5),
                    flierprops=dict(marker='o', color='red', alpha=0.5))

# New set of colors
new_colors = ['lavender', 'mediumseagreen', 'lightskyblue', 'khaki']
for i in range(0, 16, 4):
    for patch in bplots['boxes'][i:i+4]:
        patch.set_facecolor(new_colors[i // 4])

ax.set_title('Student Performance Analysis:\nQuarterly Exam Scores Across Four Classes',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Scores', fontsize=14)
ax.set_yticklabels(classes, fontsize=12)

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()