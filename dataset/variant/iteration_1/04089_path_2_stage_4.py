import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
nasa_missions = np.array([15, 16, 15, 17, 16, 18, 19, 21, 18, 19, 22])
spacex_missions = np.array([1, 2, 3, 4, 5, 7, 10, 12, 14, 18, 22])
esa_missions = np.array([10, 11, 11, 13, 12, 14, 13, 16, 15, 14, 15])
roscosmos_missions = np.array([12, 13, 12, 14, 15, 14, 13, 14, 15, 16, 16])
new_agency_missions = np.array([0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8])  # Made-up data for a new agency

data = np.vstack([nasa_missions, spacex_missions, esa_missions, roscosmos_missions, new_agency_missions])

fig, ax = plt.subplots(figsize=(14, 9))

single_color = '#1f77b4'  # Applying a single color for all data groups
ax.stackplot(years, data, colors=[single_color]*data.shape[0], alpha=0.8)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 71, 10))
ax.set_ylim(0, 70)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()