import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
video_lectures = np.array([15, 18, 21, 25, 30, 35, 40, 50, 55, 60, 65])
usage_stack = np.row_stack((video_lectures,))

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, usage_stack, colors=['#FF9999'], alpha=0.8)

ax.set_title('Changing Trends in E-Learning Resources\n(2013-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Usage Percentage (%)', fontsize=12)

plt.xticks(rotation=45)
plt.show()