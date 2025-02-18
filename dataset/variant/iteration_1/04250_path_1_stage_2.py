import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Manually altered monthly sales data: contents randomly altered
model_alpha_sales = np.array([18, 30, 5, 22, 12, 15, 9, 25, 7, 10, 28, 20])
model_beta_sales = np.array([10, 27, 8, 23, 12, 16, 13, 20, 14, 25, 6, 18])
model_gamma_sales = np.array([23, 5, 4, 18, 11, 26, 14, 21, 7, 16, 8, 12])
model_delta_sales = np.array([26, 19, 8, 32, 24, 29, 21, 14, 9, 17, 11, 13])

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF5733']
labels = ['Model Alpha', 'Model Beta', 'Model Gamma', 'Model Delta']
linestyles = ['-.', '-', ':', '--']
markers = ['d', 'o', 'v', 's']

for sales, label, color, linestyle, marker in zip(
    [model_alpha_sales, model_beta_sales, model_gamma_sales, model_delta_sales],
    labels, colors, linestyles, markers):

    ax.plot(months, sales, marker=marker, label=label, linestyle=linestyle, linewidth=2, color=color)

for sales, label, color in zip(
    [model_alpha_sales, model_beta_sales, model_gamma_sales, model_delta_sales],
    labels, colors):

    peak_month_index = np.argmax(sales)
    peak_month = months[peak_month_index]
    peak_sales = sales[peak_month_index]

    ax.annotate(
        f'{peak_sales}k units\n({peak_month})', 
        xy=(peak_month_index, peak_sales), 
        xytext=(10, 10),
        textcoords='offset points',
        arrowprops=dict(facecolor=color, shrink=0.05),
        fontsize=10, color=color, ha='center'
    )

ax.set_title('Electric Vehicle Models Sales Comparisons\nMonthly Sales in 2021', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Sales (in thousands)', fontsize=12)
ax.legend(title='EV Models', title_fontsize='13', fontsize='11', loc='upper right', frameon=False)
ax.grid(True, linestyle='-', alpha=0.3)
ax.set_xlim(-0.5, len(months)-0.5)
ax.set_ylim(0, 35)
plt.xticks(np.arange(len(months)), months, rotation=45)
plt.tight_layout()

plt.show()