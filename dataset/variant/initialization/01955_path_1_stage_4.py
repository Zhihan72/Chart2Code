import matplotlib.pyplot as plt

sectors = ['Wind Power', 'Solar Power', 'Biomass Energy', 'Geothermal Energy', 'Hydroelectric Energy', 'Nuclear Energy', 'Wave Energy']
investment_distribution = [30, 20, 15, 10, 10, 10, 5]

colors = ['#FFD700', '#FF6347', '#8A2BE2', '#4682B4', '#7CFC00', '#FFA500', '#40E0D0']
linestyles = ['-', '--', '-.', ':', '-.', '--', '-.']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    investment_distribution,
    labels=sectors,
    autopct='%1.1f%%',
    startangle=100,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='grey', linestyle=linestyles[2]),
    textprops=dict(color="navy")
)

plt.setp(autotexts, size=11, weight="heavy")

ax.set_title('Global Sector Investment in Renewable Resources for 2040', fontsize=16, fontweight='heavy', pad=30)

ax.legend(wedges, ['Wind', 'Solar', 'Bio', 'Geo', 'Hydro', 'Nuclear', 'Wave'], title="Energy Types", loc="upper right", fontsize=9, markerscale=1.5)

ax.grid(visible=True, linestyle=linestyles[1], linewidth=0.7, color='grey')
plt.gca().spines['top'].set_color('orange')
plt.gca().spines['right'].set_color('orange')

plt.tight_layout()
plt.show()