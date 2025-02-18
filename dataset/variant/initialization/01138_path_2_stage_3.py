import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
video_platform = np.array([20, 23, 29, 35, 40])  # Randomly altered label
digital_journalism = np.array([12, 13, 15, 17, 16])  # Randomly altered label
entertainment = np.array([8, 9, 10, 14, 18])  # Randomly altered label

categories = [video_platform, digital_journalism, entertainment]
shades = ['#1f77b4', '#2ca02c', '#9467bd']  # Renamed variable

plt.figure(figsize=(12, 7))
plt.stackplot(years, *categories, colors=shades, alpha=0.8)  # Used renamed variables

plt.xticks(years, fontsize=10)
plt.xlabel('Period', fontsize=12)  # Randomly altered label
plt.ylabel('Monthly Use Hours on Average', fontsize=12)  # Randomly altered label

# Title and legend (group labels) were not present originally; adding them
plt.title('Digital Activity Engagement Over Years', fontsize=14)  # Adding a title
plt.legend(labels=['Video Platform', 'Digital Journalism', 'Entertainment'], loc='upper left')  # Adding a legend with altered labels

plt.tight_layout()
plt.show()