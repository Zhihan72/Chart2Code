import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define years and data
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
social_events = np.array([5, 8, 12, 18, 25, 30, 34, 40, 48, 55, 60])
volunteer_rates = np.array([5, 8, 10, 14, 20, 28, 35, 45, 50, 58, 65])
community_budget = np.array([2, 4, 6, 10, 15, 20, 25, 32, 40, 50, 62])

# Fitting function (quadratic)
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Curve fitting
params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.scatter(social_events, volunteer_rates, color='orange', label='Participation', alpha=0.7, edgecolors='k')
ax1.plot(events_range, fitted_rates, color='blue', linestyle='-', linewidth=2, label='Fit')

# Secondary y-axis
ax2 = ax1.twinx()
ax2.bar(social_events, community_budget, color='green', alpha=0.3, label='Budget ($K)', width=1.5)

# Annotate key points
key_points = [0, 3, 6, 9]
for i in key_points:
    ax1.annotate(f'{years[i]}', (social_events[i], volunteer_rates[i]),
                 textcoords="offset points", xytext=(5, -10), ha='center', fontsize=9, color='purple')

# Titles and labels
ax1.set_title('Social Events vs. Participation', fontsize=16, pad=20)
ax1.set_xlabel('Events', fontsize=12)
ax1.set_ylabel('Participation Rate (%)', fontsize=12, color='blue')
ax2.set_ylabel('Budget ($K)', fontsize=12, color='green')

# Set limits for axes
ax1.set_xlim(0, 65)
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 70)

# Legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()