import matplotlib.pyplot as plt
import numpy as np

# Define scores for each major across various exam weeks
scores_data = {
    'Statistics': [85, 88, 83, 90, 89, 86, 84, 92, 81, 87, 85, 89, 88, 84, 85, 90, 87],
    'Chemistry': [78, 80, 79, 82, 81, 78, 84, 79, 77, 81, 80, 83, 78, 82, 80, 79, 81],
    'Mathematics': [92, 93, 91, 95, 94, 92, 90, 91, 88, 94, 93, 97, 89, 91, 92, 94, 95],
    'Biology': [88, 89, 90, 86, 87, 91, 88, 85, 84, 87, 91, 86, 90, 88, 84, 89, 86],
    'Physics': [80, 83, 78, 81, 82, 80, 79, 81, 77, 80, 83, 79, 81, 82, 78, 80, 83],
    'Computer Science': [84, 86, 88, 89, 87, 85, 86, 90, 88, 87, 85, 89, 86, 84, 86, 87, 88]
}

majors = list(scores_data.keys())
scores = list(scores_data.values())

fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Horizontal box plot
box_parts = axs[0].boxplot(scores, notch=True, vert=False, patch_artist=True, labels=majors)
new_colors = ['lightgrey', 'peachpuff', 'thistle', 'skyblue', 'khaki', 'lightgreen']
for patch, color in zip(box_parts['boxes'], new_colors):
    patch.set_facecolor(color)

# Line plot for median scores over exam weeks for each major
weeks = np.array([1, 2, 3, 4, 5, 6])
stats_median = [87, 88, 84, 86, 84, 92]
chem_median = [79, 81, 82, 80, 78, 83]
math_median = [92, 93, 89, 95, 91, 94]
bio_median = [88, 89, 91, 90, 86, 87]
phys_median = [80, 82, 80, 78, 81, 81]
cs_median = [84, 86, 89, 88, 87, 85]

median_scores_over_weeks = [stats_median, chem_median, math_median, bio_median, phys_median, cs_median]

for median_score, color in zip(median_scores_over_weeks, new_colors):
    axs[1].plot(weeks, median_score, marker='o', linestyle='-', color=color)

plt.tight_layout()
plt.show()