import matplotlib.pyplot as plt
import numpy as np

marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 5]
quarter2 = [28, 22, 25, 18, 7]
quarter3 = [35, 30, 28, 20, 12]
quarter4 = [40, 35, 30, 25, 15]

quarters = np.array([quarter1, quarter2, quarter3, quarter4])
quarters_means = np.mean(quarters, axis=0)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(marketing_strategies))

single_color = 'skyblue'

for i, quarter_data in enumerate(quarters):
    ax.bar(x_indices + i * bar_width, quarter_data, width=bar_width, color=single_color)

ax.scatter(x_indices + (bar_width * 2), quarters_means, color='black', marker='D')

ax.set_xticks(x_indices + bar_width * 1.5)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()