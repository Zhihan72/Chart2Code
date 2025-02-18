import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

children_steps = np.array([70, 75, 80, 85, 100, 110, 120, 115, 105, 90, 85, 75])
adults_steps = np.array([85, 90, 95, 100, 105, 110, 115, 110, 105, 100, 95, 90])

plt.figure(figsize=(14, 7))

plt.plot(months, children_steps, label="Kids", color='crimson', linestyle='-', marker='o', linewidth=2)
plt.plot(months, adults_steps, label="Adults", color='navy', linestyle='--', marker='s', linewidth=2)

max_steps = {"Kids": 120, "Adults": 115}
max_months = {"Kids": "Jul", "Adults": "Jul"}
for group, steps in max_steps.items():
    plt.axvline(x=max_months[group], color='darkgrey', linestyle=':', linewidth=1)
    plt.text(max_months[group], steps + 5, f'{group} Peak: {steps}K', fontsize=10, color='darkgrey')

plt.title("Steps Count by Age - 2023", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Avg Steps (k)", fontsize=12)

plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.annotate('Activity Drop', xy=("Sep", 70), xytext=("Jul", 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()

plt.show()