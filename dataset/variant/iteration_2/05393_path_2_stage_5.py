import matplotlib.pyplot as plt

age_groups = ['10-19', '20-29', '30-39', '40-49', '50+']
books_read = [8, 5, 12, 7, 9]
variability = [1.5, 1, 1.8, 1.2, 1.3]

bar_colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']

fig, ax1 = plt.subplots(figsize=(9, 8))

# Vertical bar chart
ax1.bar(age_groups, books_read, color=bar_colors, edgecolor='grey',
        yerr=variability, capsize=3)
ax1.tick_params(axis='x', labelsize=12, length=6, color='purple', direction='inout')
ax1.yaxis.grid(True, linestyle='-.', alpha=0.8)

plt.tight_layout()

plt.show()