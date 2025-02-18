import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(2010, 2020))

usage_5_14 = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
usage_15_24 = np.array([40, 50, 60, 65, 70, 75, 80, 82, 85, 88])
usage_25_34 = np.array([50, 55, 60, 65, 70, 72, 75, 78, 80, 85])
usage_35_44 = np.array([30, 35, 40, 45, 50, 55, 58, 60, 62, 65])
usage_45_plus = np.array([20, 25, 30, 35, 40, 45, 48, 50, 52, 55])

usage_data = np.vstack([usage_5_14, usage_15_24, usage_25_34, usage_35_44, usage_45_plus])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, usage_data, colors=['#ff8566', '#66ffb2', '#b266ff', '#ff8566', '#66ccff'], alpha=0.8)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()