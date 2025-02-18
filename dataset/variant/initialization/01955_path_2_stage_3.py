import matplotlib.pyplot as plt

sectors = ['Hydroelectric Energy', 'Wind Power', 'Biomass Energy', 'Solar Power', 'Geothermal Energy']
investment_distribution = [20, 25, 10, 35, 10]
colors = ['#4682B4', '#FFD700', '#8A2BE2', '#FF6347', '#7CFC00']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    investment_distribution, 
    colors=colors, 
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='black', linestyle=':')
)

# Add a grid, but since it's a pie chart, we'll make this stylistic through lines and background
ax.set_facecolor('#f0f0f5')  # Light gray background for the plot

# Randomly arranged legend
ax.legend(wedges, sectors, title="Energy Sources", loc="upper right", bbox_to_anchor=(1.1, 1))

plt.show()