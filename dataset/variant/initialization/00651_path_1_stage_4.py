import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(2010, 2020))

usage_5_14 = np.array([15, 10, 25, 20, 30, 35, 40, 50, 45, 55])
usage_15_24 = np.array([50, 40, 65, 60, 70, 82, 75, 88, 85, 80])
usage_25_34 = np.array([55, 60, 65, 70, 75, 78, 80, 72, 85, 90])
usage_35_44 = np.array([35, 30, 45, 40, 55, 50, 58, 65, 60, 62])
usage_45_plus = np.array([25, 20, 30, 35, 45, 40, 50, 52, 48, 55])

usage_data = np.vstack([usage_5_14, usage_15_24, usage_25_34, usage_35_44, usage_45_plus])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, usage_data, colors=['#ff8566', '#66ffb2', '#b266ff', '#ff8566', '#66ccff'], alpha=0.8)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()