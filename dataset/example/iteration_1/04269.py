import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Study Hours Spent by Students on Different Subjects Over a Month
# The study focuses on five subjects: Math, Science, History, Art, and Physical Education, 
# to understand the dispersion and central tendency of study hours invested by students.

# Data: Hours spent on each subject by a set of students over a month
math_hours = [20, 22, 19, 21, 23, 24, 22, 21, 25, 26, 28, 29, 18, 20, 21]
science_hours = [18, 17, 16, 19, 20, 22, 21, 19, 18, 17, 15, 14, 19, 20, 21]
history_hours = [10, 12, 11, 13, 14, 15, 13, 14, 16, 11, 10, 12, 10, 11, 12]
art_hours = [8, 9, 7, 10, 12, 15, 14, 11, 13, 13, 11, 9, 8, 10, 13]
pe_hours = [5, 6, 7, 6, 8, 9, 7, 6, 5, 4, 5, 6, 6, 7, 8]

# Combine data into a list for plotting
study_data = [math_hours, science_hours, history_hours, art_hours, pe_hours]

# Subject labels
subjects = ['Math', 'Science', 'History', 'Art', 'Physical Education']

# Create the box plot
plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(color='blue'),
                 medianprops=dict(color='red', linewidth=2),
                 whiskerprops=dict(color='black', linewidth=1.5),
                 capprops=dict(color='darkblue', linewidth=1.5),
                 flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none', markeredgecolor='orange'))

# Colors for each subject
colors = ['lavender', 'lightgreen', 'lightblue', 'pink', 'lightgoldenrodyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
plt.title('Monthly Study Hours Analysis Per Subject\nAmong High School Students', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Subjects', fontsize=12)

# Set y-tick labels
plt.yticks(range(1, len(subjects) + 1), subjects)

# Add a legend
legend_labels = subjects
plt.legend([bp["boxes"][i] for i in range(len(subjects))], legend_labels, loc='lower right')

# Display means and annotate them
means = [np.mean(data_set) for data_set in study_data]
for idx, mean in enumerate(means, start=1):
    plt.scatter(mean, idx, color='purple', zorder=3)
    plt.annotate(f'Mean: {mean:.2f}', xy=(mean, idx), xytext=(mean + 0.5, idx - 0.2),
                 fontsize=9, color='purple', arrowprops=dict(facecolor='purple', arrowstyle='->', lw=1.5))

# Add gridlines for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add a reference line for the average study time
average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axvline(average_study_time, color='blue', linestyle='--', linewidth=1.5, label=f'Overall Average: {average_study_time:.2f} hrs')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()