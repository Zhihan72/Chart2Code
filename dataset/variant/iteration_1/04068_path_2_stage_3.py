import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)
company_a = np.array([250, 100, 400, 150, 300, 500, 350, 200, 450])
company_b = np.array([180, 80, 350, 100, 300, 250, 150, 400, 220])
company_c = np.array([130, 60, 100, 260, 220, 300, 150, 80, 180])
company_d = np.array([90, 50, 170, 60, 200, 140, 110, 240, 70])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, company_a, company_b, company_c, company_d, colors=['#1f77b4'], alpha=0.8)

ax.set_title('Investment Growth of Tech Companies (2015-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Investment (Millions USD)', fontsize=12)

ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

ax.annotate('Company A R&D Surge', xy=(2020, 400), xytext=(2017, 450),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='darkorange')

ax.annotate('Company B Market Expansion', xy=(2022, 400), xytext=(2019, 300),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='royalblue')

plt.tight_layout()
plt.show()