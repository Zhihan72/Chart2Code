import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
# Swapping elements within each data group
social_events = np.array([5, 12, 8, 25, 18, 34, 30, 48, 40, 60, 55])
volunteer_rates = np.array([8, 5, 14, 10, 28, 20, 45, 35, 58, 65, 50])
community_budget = np.array([4, 2, 10, 6, 20, 15, 32, 25, 50, 62, 40])

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Re-fitting with altered data
params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.scatter(social_events, volunteer_rates, color='navy', label='Participation', alpha=0.8, edgecolors='k', marker='x')
ax1.plot(events_range, fitted_rates, color='orange', linestyle='--', linewidth=3, label='Fit')

ax2 = ax1.twinx()
ax2.bar(social_events, community_budget, color='lightgreen', alpha=0.5, label='Budget ($K)', width=2.0)

key_points = [0, 3, 6, 9]
for i in key_points:
    ax1.annotate(f'{years[i]}', (social_events[i], volunteer_rates[i]), 
                 textcoords="offset points", xytext=(0, 10), ha='right', fontsize=11, color='darkred')

ax1.set_title('Social Events vs. Participation', fontsize=16, pad=20)
ax1.set_xlabel('Events', fontsize=12)
ax1.set_ylabel('Participation Rate (%)', fontsize=12, color='orange')
ax2.set_ylabel('Budget ($K)', fontsize=12, color='lightgreen')

ax1.set_xlim(0, 65)
ax1.set_ylim(0, 80)
ax2.set_ylim(0, 80)

ax1.legend(loc='lower right', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

ax1.grid(True, linestyle='-', alpha=0.5)
ax1.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()