import matplotlib.pyplot as plt
import numpy as np

marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Influencer Collaborations', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 10, 5]
quarter2 = [28, 22, 25, 18, 15, 7]
quarter3 = [35, 30, 28, 20, 18, 12]
quarter4 = [40, 35, 30, 25, 20, 15]

quarters = np.array([quarter1, quarter2, quarter3, quarter4])
new_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']

fig, ax = plt.subplots(figsize=(12, 8))

x_indices = np.arange(len(marketing_strategies))
accumulated_heights = np.zeros(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    ax.bar(x_indices, quarter_data, bottom=accumulated_heights, color=new_colors[i], label=f'Quarter {i+1}')
    accumulated_heights += quarter_data

ax.set_xticks(x_indices)
ax.set_xticklabels(marketing_strategies)

ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()