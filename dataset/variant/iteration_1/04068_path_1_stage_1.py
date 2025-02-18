import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)
company_a = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
company_b = np.array([80, 100, 150, 180, 220, 250, 300, 350, 400])
company_c = np.array([60, 80, 100, 130, 150, 180, 220, 260, 300])
company_d = np.array([50, 60, 70, 90, 110, 140, 170, 200, 240])

data = np.vstack([company_a, company_b, company_c, company_d])
companies = ["Enterprise A", "Tech Biz B", "Innovative C", "StartUp D"]
colors = ['#FFD700', '#87CEFA', '#2E8B57', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, company_a, company_b, company_c, company_d, labels=companies, colors=colors, alpha=0.8)

ax.set_title('Tech Investment Rise: 2015-2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline Year', fontsize=12)
ax.set_ylabel('Funds in Millions USD', fontsize=12)

ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

ax.legend(loc='upper left', title='Tech Entities', fontsize=10, title_fontsize='13')

ax.annotate('R&D Boost for A', xy=(2020, 300), xytext=(2017, 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='darkorange')

ax.annotate('B Expansion Phase', xy=(2022, 350), xytext=(2019, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='royalblue')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()