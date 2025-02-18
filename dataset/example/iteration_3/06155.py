import numpy as np
import matplotlib.pyplot as plt

# Backstory: Imagine the research on "Impact of Fitness Programs Over Years" in three different cities (A, B, and C)
cities = ['City A', 'City B', 'City C']
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

# Artificial data on the number of participants in various fitness programs over the years
data = {
    'Aerobics': [50, 60, 65, 70, 90, 100, 110, 120],
    'Yoga': [40, 50, 55, 60, 70, 85, 95, 100],
    'Cardio': [60, 70, 75, 80, 85, 95, 105, 115]
}

# Create the figure and the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Positions for bars
x = np.arange(len(years))
width = 0.25

# Bar plot for each fitness program
for i, (program, counts) in enumerate(data.items()):
    ax.bar(x + i * width, counts, width, label=program)

# Setting labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Participants')
ax.set_title('Impact of Fitness Programs Over Years in Cities')
ax.set_xticks(x + width)
ax.set_xticklabels(years)

# Adding divergent information with additional subplot
ax2 = ax.twinx()

# Sample data on the retention rate (%) of each fitness program every year
retention_rate = [85, 82, 80, 78, 76, 75, 73, 71]
ax2.plot(years, retention_rate, color='red', marker='o', label='Retention Rate')
ax2.set_ylabel('Retention Rate (%)', color='red')

# Add legend and improve layout
fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.1))
fig.tight_layout(pad=3)

# Display the plot
plt.show()