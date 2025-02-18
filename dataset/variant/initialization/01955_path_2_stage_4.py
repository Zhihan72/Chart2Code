import matplotlib.pyplot as plt

sectors = ['Hydroelectric Energy', 'Wind Power', 'Biomass Energy', 'Solar Power', 'Geothermal Energy']
investment_distribution = [20, 25, 10, 35, 10]
single_color = '#4682B4'  # Consistent color for all wedges

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    investment_distribution, 
    colors=[single_color] * len(sectors), 
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='black', linestyle=':')
)

ax.set_facecolor('#f0f0f5')

ax.legend(wedges, sectors, title="Energy Sources", loc="upper right", bbox_to_anchor=(1.1, 1))

plt.show()