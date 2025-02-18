import matplotlib.pyplot as plt
import numpy as np

marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Influencer Collaborations', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 10, 5]
quarter2 = [28, 22, 25, 18, 15, 7]
quarter3 = [35, 30, 28, 20, 18, 12]
quarter4 = [40, 35, 30, 25, 20, 15]

quarters = np.array([quarter1, quarter2, quarter3, quarter4])
# Altered some colors
new_colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f']  # New color scheme

fig, ax = plt.subplots(figsize=(12, 8))

x_indices = np.arange(len(marketing_strategies))
accumulated_heights = np.zeros(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    # Changed line styles and added markers to the bars
    ax.bar(x_indices, quarter_data, bottom=accumulated_heights, color=new_colors[i],
           edgecolor='black', linewidth=1.5, hatch='/' if i % 2 == 0 else '\\',
           label=f'Quarter {i+1}')
    accumulated_heights += quarter_data

ax.set_xticks(x_indices)
ax.set_xticklabels(marketing_strategies)

# Changed grid style
ax.yaxis.grid(True, linestyle='-.', alpha=0.7, color='blue')

plt.xticks(rotation=45, ha='right')
# Moved legend location and added shadow
plt.legend(loc='upper left', shadow=True)
plt.tight_layout()

# Altered border visibility
for spine in ax.spines.values():
    spine.set_visible(True)  # Making the border visible

plt.show()