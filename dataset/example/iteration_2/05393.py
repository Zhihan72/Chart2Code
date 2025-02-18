import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In 2023, a survey titled "Reading Preferences of Different Age Groups" was conducted.
# The data comprises the average number of books read by people from different age groups 
# over the course of a year. Additionally, a pie chart shows the genre preferences of the 
# most avid readers (age 50+).

# Data for the bar chart:
age_groups = ['10-19', '20-29', '30-39', '40-49', '50+']
books_read = [5, 7, 8, 9, 12]
variability = [1, 1.5, 1.2, 1.3, 1.8]

# Data for the pie chart:
genres = ['Fiction', 'Non-fiction', 'Mystery', 'Science Fiction', 'Historical']
genre_distribution = [30, 25, 20, 15, 10]  # In percentages

# Colors for the bar chart and pie chart
bar_colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']
pie_colors = ['#ffe0b3', '#ffcc99', '#ffebcc', '#ccffe6', '#ccf2ff']

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Horizontal bar chart
bars = ax1.barh(age_groups, books_read, color=bar_colors, edgecolor='black', 
                height=0.6, xerr=variability, capsize=5)
ax1.set_title('2023 Reading Preferences Among Age Groups:\nAverage Number of Books Read Annually', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Average Number of Books Read', fontsize=12)
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 0.3, bar.get_y() + bar.get_height() / 2, f'{width} books', 
             va='center', ha='left', fontsize=10, color='darkblue')

ax1.tick_params(axis='y', labelsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Pie chart for genre preferences among 50+
ax2.pie(genre_distribution, labels=genres, autopct='%1.1f%%', startangle=90, 
        colors=pie_colors, wedgeprops={'edgecolor': 'black'})
ax2.set_title('Preferred Genres Among Avid Readers (Age 50+)', fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.4)

# Show the plot
plt.show()