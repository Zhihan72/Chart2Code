import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2026)

company_a = np.array([100, 120, 150, 140, 130, 160, 190, 210, 230, 220, 250, 270, 290, 285, 300, 310])
company_b = np.array([50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
company_c = np.array([80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380])
company_d = np.array([200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, company_a, marker='x', linestyle='-', color='#FF33A8')  # Changed to Company D's original color
ax.plot(years, company_b, marker='o', linestyle='--', color='#FF5733')  # Changed to Company A's original color
ax.plot(years, company_c, marker='*', linestyle=':', color='#33FF57')  # Changed to Company B's original color
ax.plot(years, company_d, marker='h', linestyle='-.', color='#3357FF')  # Changed to Company C's original color

ax.legend(['Company A', 'Company B', 'Company C', 'Company D'], loc='upper left')
ax.grid(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()