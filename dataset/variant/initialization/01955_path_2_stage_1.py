import matplotlib.pyplot as plt

sectors = ['Solar Power', 'Wind Power', 'Hydroelectric Energy', 'Geothermal Energy', 'Biomass Energy']
investment_distribution = [35, 25, 20, 10, 10]
colors = ['#FFD700', '#7CFC00', '#4682B4', '#FF6347', '#8A2BE2']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    investment_distribution, 
    colors=colors, 
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

plt.show()