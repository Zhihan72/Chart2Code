import matplotlib.pyplot as plt
import numpy as np

marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Influencer Collaborations', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 10, 5]
quarter2 = [28, 22, 25, 18, 15, 7]
quarter3 = [35, 30, 28, 20, 18, 12]
quarter4 = [40, 35, 30, 25, 20, 15]

quarters = np.array([quarter1, quarter2, quarter3, quarter4])
quarters_means = np.mean(quarters, axis=0)
quarter_labels = ['Q1', 'Q2', 'Q3', 'Q4']
new_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']  # Manually defined new color set

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    ax.bar(x_indices + i * bar_width, quarter_data, width=bar_width, label=quarter_labels[i], color=new_colors[i])

ax.scatter(x_indices + (bar_width * 2), quarters_means, color='black', marker='D', label='Average Impact')

ax.set_title('2023 Customer Acquisition Impact by Marketing Strategies', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Marketing Strategies', fontsize=12)
ax.set_ylabel('Customer Acquisition Impact (%)', fontsize=12)
ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(marketing_strategies, fontsize=10)

ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

legend = ax.legend(title="Quarters", loc='upper left', frameon=False, title_fontsize='11', fontsize='10')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()