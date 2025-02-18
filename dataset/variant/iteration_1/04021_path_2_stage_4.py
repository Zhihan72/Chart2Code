import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_18_24 = np.array([25, 35, 50, 58, 72, 80, 92, 94, 102, 112, 118])
age_25_34 = np.array([35, 45, 53, 75, 78, 92, 108, 128, 152, 168, 185])
age_35_44 = np.array([12, 22, 28, 42, 48, 62, 68, 78, 88, 98, 108])
age_45_54 = np.array([6, 11, 14, 21, 27, 33, 34, 38, 47, 53, 57])
age_55_plus = np.array([2, 3, 4, 6, 8, 11, 14, 13, 17, 21, 23])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, age_18_24, age_25_34, age_35_44, age_45_54, age_55_plus,
             colors=['#8A2BE2', '#7FFF00', '#DC143C', '#00FFFF', '#FF8C00'], alpha=0.8)

ax.set_title("Decade of Tech Curiosity Among Generational Waves", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Progression of Years", fontsize=12)
ax.set_ylabel("Enthusiasts in Tech (K)", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()