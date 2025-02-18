import matplotlib.pyplot as plt

age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]
single_color = '#FF9999' # Consistent color for all slices
explode = [0, 0, 0.1, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    subscriber_distribution,
    labels=None,
    colors=[single_color] * len(subscriber_distribution),  # List of the same color length matching distribution
    autopct=None,
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'width': 0.3} # Set width for donut
)

plt.tight_layout()
plt.show()