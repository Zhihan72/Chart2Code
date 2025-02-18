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

# Additional data for Class D
class_d_scores = [
    [80, 82, 84, 83, 86, 81, 85, 87, 90, 83],
    [78, 80, 82, 79, 81, 84, 83, 85, 88, 80],
    [83, 85, 87, 86, 82, 84, 86, 85, 89, 87],
    [81, 83, 82, 85, 87, 82, 84, 86, 88, 83]
]

# Combine data
data = class_a_scores + class_b_scores + class_c_scores + class_d_scores
classes = ['Exam 1 of Group A', 'Exam 2 of Group A', 'Exam III Group A', 'Exam Four\n(A)',
           'Test B 1', '2nd Exam - B', 'III B Exam', 'Fourth Group B Test',
           'Class C - Test 1', '2nd Test C', 'Exam 3 C', 'Fourth C Test',
           'Exam 1 of Group D', '2nd Exam of Group D', 'III D Exam', 'Fourth Group D Test']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(16, 10))

# Plot horizontal box plots for each class exam
bplots = ax.boxplot(data, vert=False, patch_artist=True, notch=False,
                    boxprops=dict(facecolor='lightyellow', color='blue', linewidth=1.5),
                    whiskerprops=dict(color='blue', linewidth=1.5),
                    capprops=dict(color='blue', linewidth=1.5),
                    medianprops=dict(color='red', linewidth=1.5),
                    flierprops=dict(marker='o', color='red', alpha=0.5))

# New set of colors
colors = ['skyblue', 'lightcoral', 'peachpuff', 'lightgreen']
for i in range(0, 16, 4):
    for patch in bplots['boxes'][i:i+4]:
        patch.set_facecolor(colors[i // 4])

# Set title and labels
ax.set_title('Various Tests:\n4 Groups Quarterly Exam Results', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Exam Scores', fontsize=14)
ax.set_yticklabels(classes, fontsize=12)

# Add grid for readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Optimizes layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()