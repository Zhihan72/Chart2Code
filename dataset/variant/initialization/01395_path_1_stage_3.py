import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
social_events = np.array([5, 8, 12, 18, 25, 30, 34, 40, 48, 55, 60])
volunteer_rates = np.array([10, 14, 8, 65, 20, 5, 58, 35, 28, 50, 45])
community_budget = np.array([50, 2, 6, 15, 62, 25, 10, 20, 4, 32, 40])

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

fig, ax1 = plt.subplots(figsize=(12, 7))
# Change marker style, color, and edgecolors
ax1.scatter(social_events, volunteer_rates, color='blue', marker='x', label='Actual Participation', alpha=0.7, edgecolors='g')
# Change line style and color
ax1.plot(events_range, fitted_rates, color='purple', linestyle='--', linewidth=2, label='Quadratic Fit')

ax2 = ax1.twinx()
# Change bar color
ax2.bar(social_events, community_budget, color='green', alpha=0.5, label='Community Budget ($1000s)', width=1.5)

key_points = [0, 3, 6, 9]
# Change annotation font size and color
for i in key_points:
    ax1.annotate(f'Year: {years[i]}', (social_events[i], volunteer_rates[i]),
                 textcoords="offset points", xytext=(5, -10), ha='center', fontsize=10, color='red')

# Change title alignment
ax1.set_title('Community Engagement: Social Events & Volunteer Participation', fontsize=16, pad=20, loc='right')
ax1.set_xlabel('Number of Social Events', fontsize=12)
ax1.set_ylabel('Volunteer Participation Rate (%)', fontsize=12, color='blue')
ax2.set_ylabel('Community Budget ($1000s)', fontsize=12, color='green')

ax1.set_xlim(0, 65)
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 70)

# Change legends' positions and fontsize, and turn one legend off
ax1.legend(loc='best', fontsize=11)

# Randomize grid style and border visibility
ax1.grid(True, linestyle='-', color='grey', alpha=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()