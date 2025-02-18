import matplotlib.pyplot as plt
import numpy as np

# Dataset for cyclists with altered values
months = np.arange(1, 13)
weekday_riders = np.array([35, 40, 45, 55, 50, 30, 80, 85, 60, 70, 90, 95])
weekend_riders = np.array([70, 60, 100, 90, 110, 80, 130, 120, 140, 150, 160, 170])

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(months, weekday_riders, marker='o', linestyle='-', color='blue', linewidth=2)
ax1.plot(months, weekend_riders, marker='s', linestyle='--', color='green', linewidth=2)

ax1.set_title('Comparison of Monthly Bike Enthusiasts\n(Weekday vs. Weekend)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Time of Year', fontsize=12)
ax1.set_ylabel('Cyclist Count', fontsize=12)

ax1.set_xticks(months)
ax1.set_xticklabels(['March', 'April', 'February', 'October', 'May', 'June', 'January', 'August', 'September', 'July', 'November', 'December'], fontsize=10, rotation=45)

plt.show()