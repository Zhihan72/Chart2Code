import matplotlib.pyplot as plt
import numpy as np

# Data for the number of hours secondary school students spent on extracurricular activities across different subjects in 2023
subjects = ["Sports", "Music", "Art", "Science Club", "Computer Club", "Dance", "Drama"]
hours_spent = np.array([120, 90, 80, 110, 95, 85, 100])

# Create a figure and subplots
fig, ax = plt.subplots(figsize=(12, 7))

# Create the bar chart
bar_positions = np.arange(len(subjects))
bars = ax.bar(bar_positions, hours_spent, color=['#6a0dad', '#ff6347', '#4682b4', '#3cb371', '#ff69b4', '#ffa500', '#9370db'], edgecolor='black', linewidth=1)

# Title and axis labels
ax.set_title('2023 Secondary School Students\' Time Spent on Extracurricular Activities', fontsize=16, fontweight='bold')
ax.set_xlabel('Extracurricular Activities', fontsize=14)
ax.set_ylabel('Total Hours Spent', fontsize=14)

# Setting x-tick labels orientation and their positions
ax.set_xticks(bar_positions)
ax.set_xticklabels(subjects, rotation=30, ha='right', fontsize=12)

# Annotating data labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height} hours', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, color='black')

# Adding descriptions for each activity as a legend
ax.legend(bars, [
    'Sporting activities including soccer, basketball, etc.',
    'Music classes including instruments and vocal training',
    'Art and crafts sessions',
    'Science club activities and experiments',
    'Computer club coding and tech projects',
    'Dance classes for various styles',
    'Drama club rehearsals and performances'
], title='Activity Descriptions', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize=12)

# Adding horizontal grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()