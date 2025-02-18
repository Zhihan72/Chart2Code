import matplotlib.pyplot as plt
import numpy as np

strategies = [
    'Field Sales', 'Refer-a-Friend', 'Online Marketing', 
    'Telemarketing', 'Email Campaigns', 'Retail Partnerships'
]
sales_percentages = [20, 15, 40, 10, 10, 5]
revenues = [40, 30, 80, 20, 20, 10]  # Revenue in thousands for bar plotting

x = np.arange(len(strategies))
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(12, 8))

bars1 = ax.bar(x - width/2, sales_percentages, width, label='Sales (%)', color='lightgreen', edgecolor='darkgreen')
bars2 = ax.bar(x + width/2, revenues, width, label='Revenue ($k)', color='lightblue', edgecolor='navy')

ax.set_ylabel('Percentage/Revenue ($k)', fontsize=12, labelpad=10)
ax.set_xlabel('Approaches to Sales', fontsize=12, labelpad=10)
ax.set_title('Evaluation of Sales Approaches for H1 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(strategies, rotation=45, ha='right')

# Annotate bars for sales percentages
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', va='bottom', fontsize=12, color='darkgreen')

# Annotate bars for revenue
for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'${height}k', ha='center', va='bottom', fontsize=12, color='navy')

ax.legend(loc='upper right')

plt.tight_layout()
plt.show()