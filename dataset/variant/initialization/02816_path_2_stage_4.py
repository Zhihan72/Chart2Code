import matplotlib.pyplot as plt

age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]
single_color = '#66B3FF'  # Chose a single color to apply consistently
explode = [0, 0.1, 0, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    subscriber_distribution,
    labels=age_categories,
    colors=[single_color] * len(age_categories),  # Applying the same color across all slices
    startangle=90,
    explode=explode,
    shadow=False,
    wedgeprops={'edgecolor': 'gray', 'linewidth': 0.5, 'linestyle': '--'},
    autopct='%1.1f%%'
)

centre_circle = plt.Circle((0,0),0.65,fc='lightgrey', linewidth=1.5, linestyle='-')  
fig.gca().add_artist(centre_circle)

plt.grid(visible=True, linestyle=':', color='black', linewidth=0.5)
plt.legend(title='Age Categories', loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()