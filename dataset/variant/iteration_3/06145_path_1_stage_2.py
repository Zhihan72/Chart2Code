import numpy as np
import matplotlib.pyplot as plt

# Define the subjects and alter the average study hours, manually changing some values.
subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Ed']
study_hours = np.array([6, 5, 3, 4, 1, 2])  # Altered values

# Create the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Compute study proportions
total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Plot pie chart
colors = plt.cm.Paired(np.linspace(0, 1, len(subjects)))
wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'fontsize': 12})
ax[0].set_title('Proportion of Study Time by Subject', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=12, weight='bold')
ax[0].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Plot bar chart
bars = ax[1].bar(subjects, study_hours, color='skyblue', edgecolor='black')
ax[1].set_title('Average Weekly Study Hours per Subject\nat Space Academy', fontweight='bold', fontsize=14)
ax[1].set_xlabel('Subjects', fontsize=12)
ax[1].set_ylabel('Study Hours', fontsize=12)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bars
for bar in bars:
    height = bar.get_height()
    ax[1].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 3), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=12, color='black')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()