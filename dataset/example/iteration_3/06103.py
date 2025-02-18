import matplotlib.pyplot as plt
import numpy as np

# Backstory and Data:
# We are analyzing the impact of different marketing strategies on customer acquisition across a hypothetical startup company in the year 2023.
marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Influencer Collaborations', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 10, 5]
quarter2 = [28, 22, 25, 18, 15, 7]
quarter3 = [35, 30, 28, 20, 18, 12]
quarter4 = [40, 35, 30, 25, 20, 15]

# Transforming data into arrays for easier manipulation
quarters = np.array([quarter1, quarter2, quarter3, quarter4])
quarters_means = np.mean(quarters, axis=0)
quarter_labels = ['Q1', 'Q2', 'Q3', 'Q4']
colors = plt.cm.Paired(np.linspace(0, 1, len(quarters)))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting quarterly data in grouped bar chart
bar_width = 0.2
x_indices = np.arange(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    ax.bar(x_indices + i * bar_width, quarter_data, width=bar_width, label=quarter_labels[i], color=colors[i])

# Adding data means as points
ax.scatter(x_indices + (bar_width * 2), quarters_means, color='black', marker='D', label='Average Impact')

# Title and labels
ax.set_title('2023 Customer Acquisition Impact by Marketing Strategies', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Marketing Strategies', fontsize=12)
ax.set_ylabel('Customer Acquisition Impact (%)', fontsize=12)
ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(marketing_strategies, fontsize=10)

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

# Adding legend
legend = ax.legend(title="Quarters", loc='upper left', frameon=False, title_fontsize='11', fontsize='10')

# Enhancing readability
plt.xticks(rotation=45, ha='right')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()