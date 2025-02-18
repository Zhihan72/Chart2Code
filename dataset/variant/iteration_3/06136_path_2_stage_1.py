import matplotlib.pyplot as plt
import numpy as np

activities = ['Exercise', 'Family Time', 'Education', 'Entertainment', 'Rest', 'Community Service']
time_spent = [10, 15, 20, 25, 20, 10]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0, 0, 0.2, 0, 0, 0)  # Emphasize 'Education' instead

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    time_spent, labels=activities, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='black', linestyle='--'))

plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10)

ax.set_title('Distribution of Time Spent on Weekend Activities\nin a Fictional Utopian Society in 2050', fontsize=16, weight='bold', pad=20)

plt.legend(wedges, activities, title="Activities", loc="upper right", bbox_to_anchor=(1, 1), fontsize=10, ncol=1, title_fontsize='13')

# Adding a grid on top of the pie chart just for style variety (though not common in pies)
ax.grid(True)

ax.axis('equal')
plt.tight_layout()

plt.show()