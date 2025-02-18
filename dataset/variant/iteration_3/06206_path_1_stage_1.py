import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

biking = np.array([5, 7, 8, 12, 14, 15, 16, 18, 20, 22, 25])
walking = np.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15])
public_transport = np.array([40, 38, 37, 36, 35, 34, 33, 32, 31, 30, 28])
personal_cars = np.array([30, 31, 32, 30, 30, 31, 32, 32, 32, 32, 32])

fig, ax = plt.subplots(figsize=(10, 6))

# Updated colors for the lines
ax.plot(years, biking, label='Biking', color='purple', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, walking, label='Walking', color='brown', marker='s', linestyle='--', linewidth=2, markersize=6)
ax.plot(years, public_transport, label='Public Transport', color='cyan', marker='d', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, personal_cars, label='Personal Cars', color='magenta', marker='^', linestyle=':', linewidth=2, markersize=6)

plt.title("City X Urban Transportation Trend (2010-2020)", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Usage Percentage (%)", fontsize=14)

plt.legend(title='Transportation Modes', loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title_fontsize='13')

ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(years)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()