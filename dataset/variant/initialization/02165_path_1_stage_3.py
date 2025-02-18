import matplotlib.pyplot as plt
import numpy as np

# Original data for space tourism
years = np.arange(2020, 2031)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

# New data: Projected number of Space Flights
space_flights = np.array([10, 18, 35, 60, 85, 110, 140, 185, 230, 290, 350])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot space revenue
marker_types = ['o', 's', 'D', '<']
line_styles = ['-', '--', '-.', ':']
ax1.plot(years, space_revenue, marker=marker_types[0], linestyle=line_styles[0], color='darkorange', label='Revenue ($M)')

# Plot space flights on a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, space_flights, marker=marker_types[1], linestyle=line_styles[1], color='royalblue', label='Space Flights')

# Labels and formatting
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Revenue (in millions)", fontsize=12, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')
ax2.set_ylabel("Number of Space Flights", fontsize=12, color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, max(space_revenue) + 5, 5))
ax2.set_yticks(np.arange(0, max(space_flights) + 50, 50))

milestones = {2021: "1K Tourists", 2023: "Space Hotel", 2026: "Flights Double", 2029: "30K Milestone"}
for year, label in milestones.items():
    idx = np.where(years == year)[0]
    if idx.size > 0:
        ax1.annotate(label, (years[idx[0]], space_revenue[idx[0]]), textcoords="offset points", xytext=(10, -15), ha='right', fontsize=8, arrowprops=dict(arrowstyle='->', color='green'))

ax1.grid(True, linestyle='--', alpha=0.5)

# Modify border colors
for spine in ax1.spines.values():
    spine.set_edgecolor('grey')

fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title("Space Tourism Revenue & Space Flights (2020 to 2030)", fontsize=14, fontweight='medium', pad=15)
plt.show()