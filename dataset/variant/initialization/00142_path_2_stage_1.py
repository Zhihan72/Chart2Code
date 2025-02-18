import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

italian_cuisine = [65, 68, 70, 72, 75, 80, 85, 88, 92, 95, 98]
chinese_cuisine = [70, 72, 75, 78, 80, 85, 88, 90, 92, 93, 94]
indian_cuisine = [50, 55, 60, 65, 70, 74, 80, 85, 90, 92, 95]
mexican_cuisine = [60, 63, 65, 67, 70, 73, 76, 80, 84, 87, 90]
middle_eastern_cuisine = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

width = 0.15
ind = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(ind - 2*width, italian_cuisine, width, color='tomato')
ax.bar(ind - width, chinese_cuisine, width, color='gold')
ax.bar(ind, indian_cuisine, width, color='sienna')
ax.bar(ind + width, mexican_cuisine, width, color='limegreen')
ax.bar(ind + 2*width, middle_eastern_cuisine, width, color='cornflowerblue')

# Annotate bars with popularity index values
for i, v in enumerate(italian_cuisine):
    ax.text(i - 2*width, v + 2, f"{v}", ha='center', fontsize=9, color='darkred')
for i, v in enumerate(chinese_cuisine):
    ax.text(i - width, v + 2, f"{v}", ha='center', fontsize=9, color='darkorange')
for i, v in enumerate(indian_cuisine):
    ax.text(i, v + 2, f"{v}", ha='center', fontsize=9, color='darkgoldenrod')
for i, v in enumerate(mexican_cuisine):
    ax.text(i + width, v + 2, f"{v}", ha='center', fontsize=9, color='darkgreen')
for i, v in enumerate(middle_eastern_cuisine):
    ax.text(i + 2*width, v + 2, f"{v}", ha='center', fontsize=9, color='darkblue')

# Add axis labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)

# Define x-ticks and labels
ax.set_xticks(ind)
ax.set_xticklabels(years)

plt.xticks(rotation=45)
plt.tight_layout()

# Remove borders and gridlines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Display the chart
plt.show()