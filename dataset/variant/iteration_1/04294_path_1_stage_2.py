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

ax.plot(years, football_pii, marker='o', linestyle='-', linewidth=2, color='green', label='Football')
ax.plot(years, basketball_pii, marker='s', linestyle='--', linewidth=2, color='purple', label='Basketball')
ax.plot(years, tennis_pii, marker='^', linestyle='-.', linewidth=2, color='orange', label='Tennis')
ax.plot(years, athletics_pii, marker='d', linestyle=':', linewidth=2, color='crimson', label='Athletics')
ax.plot(years, cycling_pii, marker='p', linestyle='-', linewidth=2, color='navy', label='Cycling')
ax.plot(years, swimming_pii, marker='h', linestyle='--', linewidth=2, color='teal', label='Swimming')
ax.plot(years, volleyball_pii, marker='x', linestyle='-.', linewidth=2, color='brown', label='Volleyball')

ax.set_title('Impact of Wearable Technology on Athlete Performance\nPerformance Improvement Index (PII) from 2000 to 2020', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Performance Improvement Index (PII)', fontsize=15)

ax.legend(title='Sports', loc='upper left', fontsize=12)

ax.annotate('Rapid Advancements in Tech', xy=(2015, football_pii[15]), xytext=(2008, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Tech Integration Peak', xy=(2018, athletics_pii[18]), xytext=(2011, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.show()