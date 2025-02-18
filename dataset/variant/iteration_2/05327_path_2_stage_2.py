import matplotlib.pyplot as plt
import numpy as np

# Define scores for each major across various exam weeks
scores_data = {
    'Mathematics': [85, 88, 83, 90, 89, 86, 84, 92, 81, 87, 85, 89, 88, 84, 85, 90, 87],
    'Biology': [78, 80, 79, 82, 81, 78, 84, 79, 77, 81, 80, 83, 78, 82, 80, 79, 81],
    'Computer Science': [92, 93, 91, 95, 94, 92, 90, 91, 88, 94, 93, 97, 89, 91, 92, 94, 95],
    'Chemistry': [88, 89, 90, 86, 87, 91, 88, 85, 84, 87, 91, 86, 90, 88, 84, 89, 86],
    'Physics': [80, 83, 78, 81, 82, 80, 79, 81, 77, 80, 83, 79, 81, 82, 78, 80, 83]
}

majors = list(scores_data.keys())
scores = list(scores_data.values())

fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Box plot
box = axs[0].boxplot(scores, notch=True, vert=True, patch_artist=True, labels=majors)

new_colors = ['skyblue', 'khaki', 'peachpuff', 'lightgrey', 'thistle']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)

# Line plot for median scores over exam weeks for each major
weeks = np.array([1, 2, 3, 4, 5, 6])
math_median = [85, 87, 84, 88, 90, 89]
bio_median = [78, 80, 79, 81, 83, 82]
cs_median = [92, 93, 91, 94, 95, 93]
chem_median = [88, 88, 89, 87, 90, 89]
phys_median = [80, 81, 78, 80, 82, 83]

median_scores_over_weeks = [math_median, bio_median, cs_median, chem_median, phys_median]

for median_score, color in zip(median_scores_over_weeks, new_colors):
    axs[1].plot(weeks, median_score, marker='o', linestyle='-', color=color)

plt.tight_layout()
plt.show()