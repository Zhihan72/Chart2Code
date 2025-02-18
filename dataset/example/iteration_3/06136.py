import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# "The Time Spent on Weekend Activities in a Fictional Utopian Society in 2050"
# This chart represents the distribution of time spent on various activities during weekends in a peaceful society in 2050, where people focus on balanced lifestyles and well-being.

# Define the activities and their respective time percentages (in hours)
activities = ['Exercise', 'Family Time', 'Education', 'Entertainment', 'Rest', 'Community Service']
time_spent = [10, 15, 20, 25, 20, 10]  # Adds up to 100%

# Define colors for each segment
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Define explode effect to emphasize 'Entertainment'
explode = (0, 0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    time_spent, labels=activities, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='white'))

# Customize autotexts
plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=12)

# Set title
ax.set_title('Distribution of Time Spent on Weekend Activities\nin a Fictional Utopian Society in 2050', fontsize=16, weight='bold', pad=20)

# Add a legend outside the chart
plt.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Ensure the pie is a circle
ax.axis('equal')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()