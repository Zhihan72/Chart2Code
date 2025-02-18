import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_18_24 = np.array([20, 30, 45, 60, 70, 85, 90, 95, 100, 110, 120])
age_25_34 = np.array([30, 40, 55, 70, 80, 95, 110, 130, 150, 170, 190])
age_35_44 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
age_45_54 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
age_55_plus = np.array([1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 25])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, age_18_24, age_25_34, age_35_44, age_45_54, age_55_plus,
             labels=['Young Adults', 'Mid-Age Yuppies', 'Seasoned Millennials', 'Experience Seekers', 'Golden Timers'],
             colors=['#FFD700', '#ADFF2F', '#1E90FF', '#FF69B4', '#DAA520'], alpha=0.8)

ax.set_title("Decade of Tech Curiosity Among Generational Waves", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Progression of Years", fontsize=12)
ax.set_ylabel("Enthusiasts in Tech (K)", fontsize=12)

ax.legend(loc='upper left', title='Generation Labels', fontsize=10, frameon=False)

ax.grid(True, linestyle='--', alpha=0.5)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()