import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

biking = np.array([5, 7, 8, 12, 14, 15, 16, 18, 20, 22, 25])
public_transport = np.array([40, 38, 37, 36, 35, 34, 33, 32, 31, 30, 28])
personal_cars = np.array([30, 31, 32, 30, 30, 31, 32, 32, 32, 32, 32])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, biking, color='purple', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, public_transport, color='cyan', marker='d', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, personal_cars, color='magenta', marker='^', linestyle=':', linewidth=2, markersize=6)

plt.title("Urban Travel Types (2010-2020)", fontsize=16, weight='bold', pad=20)
plt.xlabel("Timeline", fontsize=14)
plt.ylabel("Participation Rate (%)", fontsize=14)

ax.set_xticks(years)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()