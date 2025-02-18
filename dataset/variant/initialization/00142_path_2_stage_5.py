import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

italian_cuisine = [65, 68, 70, 72, 75, 80, 85, 88, 92, 95, 98]
chinese_cuisine = [70, 72, 75, 78, 80, 85, 88, 90, 92, 93, 94]
indian_cuisine = [50, 55, 60, 65, 70, 74, 80, 85, 90, 92, 95]
mexican_cuisine = [60, 63, 65, 67, 70, 73, 76, 80, 84, 87, 90]
middle_eastern_cuisine = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
japanese_cuisine = [55, 58, 60, 63, 67, 72, 78, 82, 85, 89, 92]

# Convert data to centered format
italian_center = np.array(italian_cuisine) - np.mean(italian_cuisine)
chinese_center = np.array(chinese_cuisine) - np.mean(chinese_cuisine)
indian_center = np.array(indian_cuisine) - np.mean(indian_cuisine)
mexican_center = np.array(mexican_cuisine) - np.mean(mexican_cuisine)
middle_eastern_center = np.array(middle_eastern_cuisine) - np.mean(middle_eastern_cuisine)
japanese_center = np.array(japanese_cuisine) - np.mean(japanese_cuisine)

ind = np.arange(len(years))
width = 0.5

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['cornflowerblue', 'limegreen', 'gold', 'tomato', 'sienna', 'orchid']

# Diverging bar chart
ax.bar(ind, italian_center, width, color=colors[0], label='Italian')
ax.bar(ind, chinese_center, width, color=colors[1], bottom=italian_center, label='Chinese')
ax.bar(ind, indian_center, width, color=colors[2], bottom=italian_center + chinese_center, label='Indian')
ax.bar(ind, mexican_center, width, color=colors[3], bottom=italian_center + chinese_center + indian_center, label='Mexican')
ax.bar(ind, middle_eastern_center, width, color=colors[4], bottom=italian_center + chinese_center + indian_center + mexican_center, label='Middle Eastern')
ax.bar(ind, japanese_center, width, color=colors[5], bottom=italian_center + chinese_center + indian_center + mexican_center + middle_eastern_center, label='Japanese')

ax.set_xticks(ind)
ax.set_xticklabels(years, rotation=45)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.legend()

plt.tight_layout()
plt.show()