import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

tech_idx = [40 + 3*np.sin(0.3*x) + 5*np.log(x+1) for x in range(len(years))]
env_idx = [45 + 2*np.cos(0.2*x) + 4*np.sqrt(x) for x in range(len(years))]
med_idx = [48 + 1.5*np.sin(0.2*x + np.pi/4) + 3.5*np.sqrt(x) for x in range(len(years))]
hist_idx = [35 + np.sin(0.5*x) + 2*x/10 for x in range(len(years))]
phys_idx = [50 + np.cos(0.4*x + np.pi/6) + 2.5*np.log(x+1) for x in range(len(years))]
math_idx = [38 + 1.2*np.sin(0.25*x + np.pi/3) + 2.8*np.sqrt(x) for x in range(len(years))]
astro_idx = [47 + 2.5*np.sin(0.25*x) + 3.2*x/10 for x in range(len(years))]
ling_idx = [36 + 1.8*np.cos(0.3*x + np.pi/4) + 2*x/5 for x in range(len(years))]

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

common_color = 'blue'

ax[0].plot(years, tech_idx, marker='o', linestyle='-', linewidth=2, color=common_color)
ax[0].plot(years, env_idx, marker='s', linestyle='--', linewidth=2, color=common_color)
ax[0].plot(years, med_idx, marker='^', linestyle='-.', linewidth=2, color=common_color)
ax[0].plot(years, hist_idx, marker='d', linestyle=':', linewidth=2, color=common_color)
ax[0].plot(years, phys_idx, marker='x', linestyle='-', linewidth=2, color=common_color)
ax[0].plot(years, math_idx, marker='p', linestyle='--', linewidth=2, color=common_color)
ax[0].plot(years, astro_idx, marker='*', linestyle='-', linewidth=2, color=common_color)
ax[0].plot(years, ling_idx, marker='h', linestyle='--', linewidth=2, color=common_color)

ax[0].set_xlabel('Year')
ax[0].set_ylabel('Index')
ax[0].set_title('Knowledge Growth (2000-2030)', fontweight='bold')

ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].spines['left'].set_visible(False)

ax[0].annotate('Tech Peak', xy=(2025, tech_idx[25]), xytext=(2018, 80),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)
ax[0].annotate('Med High', xy=(2015, med_idx[15]), xytext=(2008, 65),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

moving_avg = np.convolve(tech_idx, np.ones(5)/5, mode='valid')

ax[1].plot(years[2:-2], moving_avg, color=common_color, linestyle='-', linewidth=2)

ax[1].set_xlabel('Year')
ax[1].set_ylabel('5-Year Avg')
ax[1].set_title('Tech Trend Summary', fontweight='bold')

ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(False)
ax[1].spines['left'].set_visible(False)

plt.tight_layout()
plt.show()