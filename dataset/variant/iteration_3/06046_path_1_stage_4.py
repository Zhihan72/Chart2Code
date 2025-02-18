import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
company_a_users = np.array([5, 10, 18, 30, 45, 63, 85, 110, 139, 171, 205, 243, 284, 328, 375, 425, 478, 534, 593, 655, 720])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, company_a_users, marker='o', linestyle='-', color='tomato', linewidth=2, markersize=6)

ax1.annotate('100M Users for Company A Reached', xy=(2007, 100), xytext=(2003, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.axvline(x=2020, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(2021, 750, 'Peak Users Year 2020', rotation=90, verticalalignment='center', fontsize=10, color='gray')

ax1.set_title("Tech Giants Rise: Growth of User Numbers (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Years", fontsize=12)
ax1.set_ylabel("Users (Millions)", fontsize=12)

plt.tight_layout()
plt.show()