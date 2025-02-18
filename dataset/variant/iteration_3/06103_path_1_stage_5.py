import matplotlib.pyplot as plt
import numpy as np

# Updated marketing strategies without 'Influencer Collaborations'
marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 5]  # Removed the data for 'Influencer Collaborations'
quarter2 = [28, 22, 25, 18, 7]  # Removed the data for 'Influencer Collaborations'
quarter3 = [35, 30, 28, 20, 12] # Removed the data for 'Influencer Collaborations'
quarter4 = [40, 35, 30, 25, 15] # Removed the data for 'Influencer Collaborations'

quarters = np.array([quarter1, quarter2, quarter3, quarter4])
new_colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f']

fig, ax = plt.subplots(figsize=(12, 8))

x_indices = np.arange(len(marketing_strategies))
accumulated_heights = np.zeros(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    ax.bar(x_indices, quarter_data, bottom=accumulated_heights, color=new_colors[i],
           edgecolor='black', linewidth=1.5, hatch='/' if i % 2 == 0 else '\\',
           label=f'Quarter {i+1}')
    accumulated_heights += quarter_data

ax.set_xticks(x_indices)
ax.set_xticklabels(marketing_strategies)
ax.yaxis.grid(True, linestyle='-.', alpha=0.7, color='blue')

plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper left', shadow=True)
plt.tight_layout()

for spine in ax.spines.values():
    spine.set_visible(True)

plt.show()