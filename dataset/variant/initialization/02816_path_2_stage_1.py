import matplotlib.pyplot as plt

age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6961', '#77DD77']
explode = [0, 0, 0.1, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    subscriber_distribution,
    labels=None,  # Remove text labels from the slices
    colors=colors,
    autopct=None,  # Remove percentage labels
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

plt.tight_layout()
plt.show()