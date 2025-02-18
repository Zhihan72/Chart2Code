import matplotlib.pyplot as plt

working_hours = {
    "SW Eng": [40, 42, 38, 45, 50, 35, 40, 38, 42, 48, 44, 46, 37, 39, 41, 43],
    "Docs": [50, 55, 60, 52, 58, 62, 48, 54, 57, 63, 56, 59, 53, 51, 49, 47],
    "Tchrs": [30, 32, 29, 35, 34, 37, 33, 28, 31, 36, 32, 30, 29, 33, 34, 35],
    "Lawrs": [45, 48, 52, 55, 50, 46, 49, 53, 47, 51, 54, 48, 50, 52, 47, 49]
}

professions = list(working_hours.keys())
data = list(working_hours.values())

fig, ax = plt.subplots(figsize=(8, 8))

ax.boxplot(data, vert=False, patch_artist=True, labels=professions, notch=True,
           boxprops=dict(facecolor='#a6cee3', color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'),
           medianprops=dict(color='darkred', linewidth=2))

ax.set_xlabel("Hours", fontsize=12)
ax.set_ylabel("Jobs", fontsize=12)

plt.tight_layout()
plt.show()