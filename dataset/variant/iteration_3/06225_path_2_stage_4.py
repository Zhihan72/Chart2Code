import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

children_steps = np.array([70, 75, 80, 85, 100, 110, 120, 115, 105, 90, 85, 75])
adults_steps = np.array([85, 90, 95, 100, 105, 110, 115, 110, 105, 100, 95, 90])

plt.figure(figsize=(14, 7))

plt.plot(months, children_steps, color='crimson', linestyle='-', marker='o', linewidth=2)
plt.plot(months, adults_steps, color='navy', linestyle='--', marker='s', linewidth=2)

plt.title("Steps Count by Age - 2023", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Avg Steps (k)", fontsize=12)

plt.annotate('Activity Drop', xy=("Sep", 70), xytext=("Jul", 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()

plt.show()