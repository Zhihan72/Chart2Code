import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

trees = np.array([50, 52, 54, 58, 64, 70, 75, 80, 85, 87, 89, 90, 92, 94, 95, 97, 98, 100, 103, 107, 110])
shrubs = np.array([30, 32, 34, 36, 38, 40, 44, 48, 50, 53, 56, 58, 60, 64, 68, 72, 76, 78, 80, 82, 85])
wildflowers = np.array([20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180])
ferns = np.array([10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 34, 36, 38, 40, 42, 44, 46, 50, 54, 56, 58])
grasses = np.array([5, 7, 9, 13, 16, 20, 25, 30, 35, 40, 42, 44, 46, 48, 52, 54, 56, 58, 60, 62, 65])

flora_data = np.vstack([trees, shrubs, wildflowers, ferns, grasses])

fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(years, flora_data, colors=['#FF6347', '#3CB371', '#4682B4', '#DAA520', '#8A2BE2'], alpha=0.7)

ax.set_title("Flora Diversity in FloraLand (2000-2020):\nA Journey of Conservation and Growth", 
             fontsize=18, weight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Species", fontsize=14)
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)
ax.set_yticks(np.arange(0, 321, 40))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.annotate("Major Reforestation Efforts", xy=(2008, 90), xytext=(2005, 250),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkgreen'), fontsize=12, color='darkgreen')

ax.annotate("Shrubland Recovery Program", xy=(2014, 64), xytext=(2010, 300),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='olive'), fontsize=12, color='olive')

ax.annotate("Wildflower Meadow Initiative", xy=(2018, 150), xytext=(2015, 340),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='gold'), fontsize=12, color='gold')

plt.tight_layout()
plt.show()