import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

company_a_users = np.array([5, 10, 18, 30, 45, 63, 85, 110, 139, 171, 205, 243, 284, 328, 375, 425, 478, 534, 593, 655, 720])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, company_a_users, label='Company A Users', marker='o', linestyle='-', color='mediumseagreen', linewidth=2, markersize=6)

ax1.annotate('Company A hits 100M users', xy=(2007, 100), xytext=(2003, 150),
             arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.5),
             fontsize=10, fontweight='bold', color='mediumseagreen')

ax1.axvline(x=2020, color='darkgray', linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(2021, 750, '2020 Peak Users', rotation=90, verticalalignment='center', fontsize=10, color='darkgray')

ax1.set_title("Rise of Tech Giants: Number of Users Growth (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Users (in Millions)", fontsize=12)

ax1.legend(loc='upper left', fontsize=10, title="Company", frameon=True)

ax1.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()