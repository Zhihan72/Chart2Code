import matplotlib.pyplot as plt

age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#66FF66', '#FFBB99']
explode = [0, 0.1, 0, 0.1, 0, 0, 0.1]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    subscriber_distribution,
    labels=age_categories,  # Adding legend-like labels directly on the pie chart
    colors=colors,  # Different colors for each slice
    autopct='%1.1f%%',
    startangle=180,
    explode=explode,
    shadow=False,  # Remove shadow for visual clarity
    wedgeprops={'edgecolor': 'darkgrey', 'linewidth': 2, 'linestyle': '--', 'width': 0.4}  # Different edge style
)

ax.set_title('Subscriber Distribution by Age', fontsize=14, fontweight='bold')
plt.grid(visible=True, linestyle='-', linewidth=0.5, alpha=0.5)  # Add grid to the background
plt.tight_layout()
plt.show()