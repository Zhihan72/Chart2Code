import matplotlib.pyplot as plt
import numpy as np

# Month labels for the year 2021
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Monthly sales data (in thousands) for the EV models
model_alpha_sales = np.array([5, 7, 9, 10, 12, 15, 18, 20, 22, 25, 28, 30])
model_beta_sales = np.array([6, 8, 10, 12, 13, 14, 16, 18, 20, 23, 25, 27])
model_gamma_sales = np.array([4, 5, 7, 8, 11, 12, 14, 16, 18, 21, 23, 26])
model_delta_sales = np.array([8, 9, 11, 13, 14, 17, 19, 21, 24, 26, 29, 32])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each EV model
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF5733']
labels = ['Model Alpha', 'Model Beta', 'Model Gamma', 'Model Delta']
linestyles = ['-.', '-', ':', '--']
markers = ['d', 'o', 'v', 's']

for sales, label, color, linestyle, marker in zip(
    [model_alpha_sales, model_beta_sales, model_gamma_sales, model_delta_sales],
    labels, colors, linestyles, markers):

    ax.plot(months, sales, marker=marker, label=label, linestyle=linestyle, linewidth=2, color=color)

# Annotate the peak sales month for each model
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

# Title and labels
ax.set_title('Electric Vehicle Models Sales Comparisons\nMonthly Sales in 2021', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Sales (in thousands)', fontsize=12)

# Customize legend
ax.legend(title='EV Models', title_fontsize='13', fontsize='11', loc='upper right', frameon=False)

# Modify grid lines
ax.grid(True, linestyle='-', alpha=0.3)

# Set limits for x-axis and y-axis
ax.set_xlim(-0.5, len(months)-0.5)
ax.set_ylim(0, 35)

# Customize the x-axis ticks for clarity
plt.xticks(np.arange(len(months)), months, rotation=45)
plt.tight_layout()

# Show the plot
plt.show()