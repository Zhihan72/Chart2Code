import matplotlib.pyplot as plt

age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6961', '#77DD77']
explode = [0, 0, 0.1, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    subscriber_distribution,
    labels=None,
    colors=colors,
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Add a circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()