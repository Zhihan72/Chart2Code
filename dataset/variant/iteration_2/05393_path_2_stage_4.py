import matplotlib.pyplot as plt

age_groups = ['10-19', '20-29', '30-39', '40-49', '50+']
books_read = [8, 5, 12, 7, 9]
variability = [1.5, 1, 1.8, 1.2, 1.3]

genre_distribution = [15, 30, 10, 25, 20]

bar_colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']
pie_colors = ['#ffe0b3', '#ffcc99', '#ffebcc', '#ccffe6', '#ccf2ff']

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Vertical bar chart
ax1.bar(age_groups, books_read, color=bar_colors, edgecolor='grey',
        yerr=variability, capsize=3)
ax1.tick_params(axis='x', labelsize=12, length=6, color='purple', direction='inout')
ax1.yaxis.grid(True, linestyle='-.', alpha=0.8)

ax2.pie(genre_distribution, startangle=45, colors=pie_colors, wedgeprops={'edgecolor': 'grey'},
        explode=(0.1, 0, 0, 0, 0), labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%')

plt.tight_layout()
plt.subplots_adjust(wspace=0.2)

plt.show()