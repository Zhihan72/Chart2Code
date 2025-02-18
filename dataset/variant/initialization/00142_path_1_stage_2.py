import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

italian_cuisine = [65, 68, 70, 72, 75, 80, 85, 88, 92, 95, 98]
chinese_cuisine = [70, 72, 75, 78, 80, 85, 88, 90, 92, 93, 94]
indian_cuisine = [50, 55, 60, 65, 70, 74, 80, 85, 90, 92, 95]
mexican_cuisine = [60, 63, 65, 67, 70, 73, 76, 80, 84, 87, 90]
middle_eastern_cuisine = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Additional made-up data
japanese_cuisine = [40, 42, 45, 48, 52, 56, 60, 65, 70, 75, 78]
french_cuisine = [50, 53, 57, 60, 64, 69, 73, 77, 81, 86, 89]

width = 0.1
ind = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# Updated with additional cuisines
ax.bar(ind - 3*width, italian_cuisine, width, label='Italian', color='skyblue')
ax.bar(ind - 2*width, chinese_cuisine, width, label='Chinese', color='purple')
ax.bar(ind - width, indian_cuisine, width, label='Indian', color='salmon')
ax.bar(ind, mexican_cuisine, width, label='Mexican', color='peru')
ax.bar(ind + width, middle_eastern_cuisine, width, label='Middle-Eastern', color='pink')
ax.bar(ind + 2*width, japanese_cuisine, width, label='Japanese', color='lightgreen')
ax.bar(ind + 3*width, french_cuisine, width, label='French', color='gold')

# Updated annotations
for i, v in enumerate(italian_cuisine):
    ax.text(i - 3*width, v + 2, f"{v}", ha='center', fontsize=9, color='navy')
for i, v in enumerate(chinese_cuisine):
    ax.text(i - 2*width, v + 2, f"{v}", ha='center', fontsize=9, color='indigo')
for i, v in enumerate(indian_cuisine):
    ax.text(i - width, v + 2, f"{v}", ha='center', fontsize=9, color='darkred')
for i, v in enumerate(mexican_cuisine):
    ax.text(i, v + 2, f"{v}", ha='center', fontsize=9, color='darkorange')
for i, v in enumerate(middle_eastern_cuisine):
    ax.text(i + width, v + 2, f"{v}", ha='center', fontsize=9, color='deeppink')
for i, v in enumerate(japanese_cuisine):
    ax.text(i + 2*width, v + 2, f"{v}", ha='center', fontsize=9, color='green')
for i, v in enumerate(french_cuisine):
    ax.text(i + 3*width, v + 2, f"{v}", ha='center', fontsize=9, color='goldenrod')

ax.set_title('Culinary Trends in Global Cuisine Preferences\n(2010-2020)', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)
ax.set_xticks(ind)
ax.set_xticklabels(years)
ax.legend(title='Cuisine Type', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()