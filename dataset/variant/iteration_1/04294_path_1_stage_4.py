import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
football_pii = [50 + 3*np.sin(0.2*x) + 2*x for x in range(len(years))]
basketball_pii = [45 + 2.5*np.cos(0.15*x) + 2.1*x for x in range(len(years))]
tennis_pii = [48 + 2.8*np.sin(0.18*x + np.pi/6) + 1.8*x for x in range(len(years))]
athletics_pii = [55 + 3.2*np.sin(0.2*x) + 2.5*x for x in range(len(years))]
cycling_pii = [40 + 3.5*np.cos(0.2*x + np.pi/4) + 2.3*x for x in range(len(years))]
swimming_pii = [42 + 3*np.sin(0.16*x) + 2.2*x for x in range(len(years))]
volleyball_pii = [44 + 2.7*np.cos(0.18*x) + 2*x for x in range(len(years))]

fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(years, football_pii, marker='x', linestyle='-.', linewidth=1.5, color='blue')
ax.plot(years, basketball_pii, marker='p', linestyle='-', linewidth=1.5, color='orange')
ax.plot(years, tennis_pii, marker='s', linestyle='--', linewidth=1.5, color='red')
ax.plot(years, athletics_pii, marker='h', linestyle='-', linewidth=1.5, color='darkgreen')
ax.plot(years, cycling_pii, marker='d', linestyle=':', linewidth=1.5, color='purple')
ax.plot(years, swimming_pii, marker='^', linestyle='--', linewidth=1.5, color='cyan')
ax.plot(years, volleyball_pii, marker='o', linestyle='-', linewidth=1.5, color='magenta')

ax.grid(True, linestyle='-', alpha=0.5)
ax.set_facecolor('#e0e0e0')

plt.tight_layout()
plt.show()