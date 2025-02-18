import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

italian_cuisine = [65, 68, 70, 72, 75, 80, 85, 88, 92, 95, 98]
chinese_cuisine = [70, 72, 75, 78, 80, 85, 88, 90, 92, 93, 94]
indian_cuisine = [50, 55, 60, 65, 70, 74, 80, 85, 90, 92, 95]
mexican_cuisine = [60, 63, 65, 67, 70, 73, 76, 80, 84, 87, 90]
middle_eastern_cuisine = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
japanese_cuisine = [55, 58, 60, 63, 67, 72, 78, 82, 85, 89, 92]

width = 0.15
ind = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['cornflowerblue', 'limegreen', 'gold', 'tomato', 'sienna', 'orchid']

ax.bar(ind - 2.5*width, italian_cuisine, width, color=colors[0])
ax.bar(ind - 1.5*width, chinese_cuisine, width, color=colors[1])
ax.bar(ind - 0.5*width, indian_cuisine, width, color=colors[2])
ax.bar(ind + 0.5*width, mexican_cuisine, width, color=colors[3])
ax.bar(ind + 1.5*width, middle_eastern_cuisine, width, color=colors[4])
ax.bar(ind + 2.5*width, japanese_cuisine, width, color=colors[5])

# Remove textual annotations and labels

ax.set_xticks(ind)
ax.set_xticklabels([])
plt.xticks(rotation=45)
plt.tight_layout()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()