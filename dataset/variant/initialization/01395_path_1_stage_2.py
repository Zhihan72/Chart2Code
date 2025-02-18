import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
social_events = np.array([5, 8, 12, 18, 25, 30, 34, 40, 48, 55, 60])

# Manually shuffled values
volunteer_rates = np.array([10, 14, 8, 65, 20, 5, 58, 35, 28, 50, 45])
community_budget = np.array([50, 2, 6, 15, 62, 25, 10, 20, 4, 32, 40])

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.scatter(social_events, volunteer_rates, color='orange', label='Actual Participation', alpha=0.7, edgecolors='k')
ax1.plot(events_range, fitted_rates, color='orange', linestyle='-', linewidth=2, label='Quadratic Fit')

ax2 = ax1.twinx()
ax2.bar(social_events, community_budget, color='orange', alpha=0.3, label='Community Budget ($1000s)', width=1.5)

key_points = [0, 3, 6, 9]
for i in key_points:
    ax1.annotate(f'Year: {years[i]}', (social_events[i], volunteer_rates[i]),
                 textcoords="offset points", xytext=(5, -10), ha='center', fontsize=9, color='purple')

ax1.set_title('Community Engagement: Correlation Between Social Events and Volunteer Participation', fontsize=16, pad=20)
ax1.set_xlabel('Number of Social Events', fontsize=12)
ax1.set_ylabel('Volunteer Participation Rate (%)', fontsize=12, color='orange')
ax2.set_ylabel('Community Budget ($1000s)', fontsize=12, color='orange')

ax1.set_xlim(0, 65)
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 70)

ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()