import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)
company_a = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
company_b = np.array([80, 100, 150, 180, 220, 250, 300, 350, 400])
company_c = np.array([60, 80, 100, 130, 150, 180, 220, 260, 300])
company_d = np.array([50, 60, 70, 90, 110, 140, 170, 200, 240])
company_e = np.array([30, 50, 80, 120, 160, 190, 230, 270, 320])
company_f = np.array([20, 40, 60, 95, 125, 145, 180, 210, 250])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'] 
data = np.vstack([company_a, company_b, company_c, company_d, company_e, company_f])
companies = ["Enterprise A", "Tech Biz B", "Innovative C", "StartUp D", "Venture E", "Growth F"]

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, company_a, company_b, company_c, company_d, company_e, company_f, labels=companies, colors=colors, alpha=0.7)

ax.set_title('Tech Investment Growth: 2015-2023', fontsize=18, fontweight='heavy', pad=25)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Investments (Million USD)', fontsize=14)

ax.set_xticks(years)
ax.tick_params(axis='x', rotation=30, labelsize=10)

ax.legend(loc='lower right', title='Companies', fontsize=11, title_fontsize='14', facecolor='lightgrey')

ax.annotate('Significant Rise in A', xy=(2020, 300), xytext=(2016, 330),
            arrowprops=dict(arrowstyle='-|>', lw=2, color='green'),
            fontsize=11, color='teal')

ax.annotate('B Reached New Heights', xy=(2022, 350), xytext=(2018, 420),
            arrowprops=dict(arrowstyle='-|>', lw=2, color='purple'),
            fontsize=11, color='navy')

ax.grid(True, which='major', linestyle='-.', linewidth=0.8)

plt.tight_layout()

plt.show()