import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
company_a_users = np.array([5, 10, 18, 30, 45, 63, 85, 110, 139, 171, 205, 243, 284, 328, 375, 425, 478, 534, 593, 655, 720])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Changed the line style, color, and marker type
ax1.plot(years, company_a_users, label='Company A Users', marker='^', linestyle='--', color='royalblue', linewidth=2.5, markersize=8)

# Modified annotation style and color
ax1.annotate('Company A hits 100M users', xy=(2007, 100), xytext=(2003, 150),
             arrowprops=dict(facecolor='black', arrowstyle='-|>', lw=1.8),
             fontsize=10, fontweight='bold', color='royalblue')

# Changed the vertical line color, style, and added a border
ax1.axvline(x=2020, color='indianred', linestyle='-.', linewidth=2, alpha=0.8)
ax1.text(2021, 750, '2020 Peak Users', rotation=90, verticalalignment='center', fontsize=10, color='indianred')

# Modified title padding and color
ax1.set_title("Rise of Tech Giants: Number of Users Growth (2000-2020)", fontsize=16, fontweight='bold', pad=30, color='darkblue')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Users (in Millions)", fontsize=12)

# Changed legend placement and frame settings
ax1.legend(loc='lower right', fontsize=11, title="Company", frameon=False)

# Modified grid style and intensity
ax1.grid(True, which='both', linestyle='-.', linewidth=0.7, alpha=0.6)

plt.tight_layout()
plt.show()