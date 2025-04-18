import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
swimmer_assist = np.array([50, 45, 60, 55, 65])
minor_injuries = np.array([20, 25, 15, 18, 22])
major_injuries = np.array([5, 4, 6, 7, 6])

rescue_data = np.vstack([swimmer_assist, minor_injuries, major_injuries])

fig, ax = plt.subplots(figsize=(14, 8))
# Apply a single color (#87CEEB) consistently across all data groups
ax.stackplot(years, rescue_data, colors=['#87CEEB', '#87CEEB', '#87CEEB'], alpha=0.85)

highlight_years = [2019, 2021]
for year in highlight_years:
    ax.axvline(x=year, color='gray', linestyle='-.', linewidth=1.5)

ax.grid(visible=True, linestyle=':', alpha=0.5)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=40, ha='right')

# Change plot lines to use a single color for consistency
for y in rescue_data:
    ax.plot(years, y, marker='d', markersize=7, color='#87CEEB', linestyle='-', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()