import matplotlib.pyplot as plt
import numpy as np

budget_categories = [
    'Metropolitan Initiatives',
    'Medical Outreach Projects',
    'Innovative Tech Fields',
    'Educational Scholarships',
    'Community Security',
    'Eco-Friendly Polices',
    'Cultural Heritage',
    'Commute Systems',
    'Galaxy Probes',
    'Quantum Physics Studies'
]

budget_allocation = [20, 18, 15, 12, 10, 6, 4, 2, 8, 5]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD433', '#FF6666', '#66CCCC', '#93FF33', '#CC99FF', '#33FFCC']
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(2, 1, figsize=(12, 12))

ax[0].pie(
    budget_allocation, explode=explode, labels=budget_categories, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85
)

ax[0].set_title("Zyphon Fiscal Resources Allocation (Theta Era)", fontsize=16, fontweight='bold', pad=20)

years = np.arange(3000, 3051, 10)
tech_advancement = {
    'Autonomous Machines': np.array([10, 15, 20, 25, 35, 40]),
    'Renewable Power': np.array([5, 10, 15, 20, 30, 38]),
    'Genetic Engineering': np.array([8, 12, 18, 23, 27, 33]),
    'Quantum Algorithms': np.array([2, 7, 12, 18, 25, 32]),
    'Cosmic Technology': np.array([3, 6, 10, 15, 22, 28])
}

for tech, improvements in tech_advancement.items():
    ax[1].plot(years, improvements, marker='o', linewidth=2.5)

ax[1].set_title('Evolution of Tech Domains (Eon 3000-3050)', fontsize=16, fontweight='bold', pad=20)
ax[1].set_xlabel('Chronological Marker', fontsize=12, fontweight='bold')
ax[1].set_ylabel('Innovation Index', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()