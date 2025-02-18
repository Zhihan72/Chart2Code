import numpy as np
import matplotlib.pyplot as plt

# Define the subjects and average study hours.
subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Ed']
study_hours = np.array([5, 6, 4, 3, 2, 1])

# Creating the main figure and axis
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Data for the pie chart subplot to show distribution of total weekly study time
total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Plotting the pie chart first
colors = plt.cm.Paired(np.linspace(0, 1, len(subjects)))
wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'fontsize': 12})
ax[0].set_title('Proportion of Study Time by Subject', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=12, weight='bold')
ax[0].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Plotting the bar chart second
bars = ax[1].bar(subjects, study_hours, color='skyblue', edgecolor='black')
ax[1].set_title('Average Weekly Study Hours per Subject\nat Space Academy', fontweight='bold', fontsize=14)
ax[1].set_xlabel('Subjects', fontsize=12)
ax[1].set_ylabel('Study Hours', fontsize=12)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotating study hours on top of each bar
for bar in bars:
    height = bar.get_height()
    ax[1].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 3), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=12, color='black')

# Adjusting the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()