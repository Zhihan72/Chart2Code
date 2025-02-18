import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
adults_steps = np.array([85, 90, 95, 100, 105, 110, 115, 110, 105, 100, 95, 90])
seniors_steps = np.array([50, 55, 60, 65, 70, 75, 80, 75, 70, 65, 60, 55])

plt.figure(figsize=(14, 7))
plt.plot(months, adults_steps, color='tab:blue', linestyle='--', marker='s', linewidth=2)
plt.plot(months, seniors_steps, color='tab:red', linestyle='-.', marker='^', linewidth=2)

plt.title("Monthly Steps Count Analysis\nfor Different Age Groups - Year 2023", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Monthly Steps (in thousands)", fontsize=12)

plt.tight_layout()
plt.show()