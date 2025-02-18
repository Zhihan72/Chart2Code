import numpy as np
import matplotlib.pyplot as plt

# Backstory: This bar chart visualizes the average amount of time (in hours) study was dedicated to different subjects in a week by high school students in a fictional school, Space Academy. We will also include a subplot showing the total weekly study time in a pie chart.

# Define the subjects and average study hours. 
subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Ed']
study_hours = np.array([5, 6, 4, 3, 2, 1])

# Creating the main figure and axis
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the bar chart
bars = ax[0].bar(subjects, study_hours, color='skyblue', edgecolor='black')

# Adding titles, labels, and customizing the first subplot
ax[0].set_title('Average Weekly Study Hours per Subject\nat Space Academy', fontweight='bold', fontsize=14)
ax[0].set_xlabel('Subjects', fontsize=12)
ax[0].set_ylabel('Study Hours', fontsize=12)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotating study hours on top of each bar
for bar in bars:
    height = bar.get_height()
    ax[0].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 3), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=12, color='black')

# Data for the pie chart subplot to show distribution of total weekly study time
total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Plotting the pie chart
colors = plt.cm.Paired(np.linspace(0, 1, len(subjects)))
wedges, texts, autotexts = ax[1].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'fontsize': 12})

# Customizing the second subplot
ax[1].set_title('Proportion of Study Time by Subject', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=12, weight='bold')
ax[1].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjusting the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()