import matplotlib.pyplot as plt

sectors = ['Hydroelectric Energy', 'Wind Power', 'Biomass Energy', 'Solar Power', 'Geothermal Energy']
investment_distribution = [20, 25, 10, 35, 10]
colors = ['#4682B4', '#7CFC00', '#8A2BE2', '#FFD700', '#FF6347']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    investment_distribution, 
    colors=colors, 
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

plt.show()