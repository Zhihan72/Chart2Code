import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
video_platform = np.array([20, 23, 29, 35, 40])
digital_journalism = np.array([12, 13, 15, 17, 16])
entertainment = np.array([8, 9, 10, 14, 18])

categories = [video_platform, digital_journalism, entertainment]
new_shades = ['#ff7f0e', '#d62728', '#8c564b']  # A new set of colors

plt.figure(figsize=(12, 7))
plt.stackplot(years, *categories, colors=new_shades, alpha=0.8)

plt.xticks(years, fontsize=10)
plt.xlabel('Period', fontsize=12)
plt.ylabel('Monthly Use Hours on Average', fontsize=12)

plt.title('Digital Activity Engagement Over Years', fontsize=14)
plt.legend(labels=['Video Platform', 'Digital Journalism', 'Entertainment'], loc='upper left')

plt.tight_layout()
plt.show()