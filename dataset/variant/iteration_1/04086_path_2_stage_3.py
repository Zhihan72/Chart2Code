import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

crews = ["Beta", "Delta", "Epsilon", "Gamma", "Alpha", "Theta", "Eta"]
epochs = np.arange(2015, 2022)

efficiency_data = np.array([
    [72, 78, 81, 85, 88, 90, 93],
    [70, 75, 78, 82, 84, 86, 90],
    [65, 68, 72, 75, 79, 82, 85],
    [68, 73, 72, 76, 79, 83, 88],
    [65, 70, 75, 80, 78, 82, 87],
    [66, 70, 73, 76, 79, 81, 84],
    [67, 70, 74, 78, 81, 83, 87]
]).T 

average_efficiency = np.mean(efficiency_data, axis=0)

fig = plt.figure(figsize=(18, 10))
gs = gridspec.GridSpec(2, 2, height_ratios=[4, 1], width_ratios=[4, 1])

ax1 = plt.subplot(gs[:, 0])
heatmap1 = ax1.imshow(efficiency_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

ax1.set_title("Crew Efficiency Over the Ages at Tech Breakthroughs Inc.", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Crews', fontsize=12)
ax1.set_ylabel('Epoch', fontsize=12)
ax1.set_xticks(np.arange(len(crews)))
ax1.set_xticklabels(crews, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(epochs)))
ax1.set_yticklabels(epochs)

cbar1 = plt.colorbar(heatmap1, ax=ax1, orientation='vertical')
cbar1.set_label('Monthly Efficiency Score', fontsize=12)

for i in range(len(epochs)):
    for j in range(len(crews)):
        ax1.text(j, i, efficiency_data[i, j], ha='center', va='center', color='black', fontsize=8)

ax2 = plt.subplot(gs[1, 1])
colors = ['#FF5733', '#33FFCE', '#A033FF', '#FFBD33', '#338BFF', '#FF33E3', '#FF339D']  # Adjusted colors list
bar_chart = ax2.barh(crews, average_efficiency, color=colors, edgecolor='black')
ax2.set_title('Average Efficiency Score per Crew (2015-2021)', fontsize=12, pad=10)
ax2.set_xlabel('Average Efficiency Score', fontsize=10)
ax2.set_xlim(60, 95)

for bar in bar_chart:
    width = bar.get_width()
    ax2.text(width - 4, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', va='center', ha='center', color='black', fontsize=10)

yearly_trend = np.diff(efficiency_data, axis=0)
ax3 = plt.subplot(gs[0, 1])
heatmap2 = ax3.imshow(yearly_trend, cmap='coolwarm', aspect='auto', interpolation='nearest')

ax3.set_title("Year-to-Year Efficiency Change", fontsize=12, pad=10)
ax3.set_xlabel('Crews', fontsize=10)
ax3.set_ylabel('Epoch Difference', fontsize=10)
ax3.set_xticks(np.arange(len(crews)))
ax3.set_xticklabels(crews, rotation=45, ha='right')
ax3.set_yticks(np.arange(1, len(epochs)))
ax3.set_yticklabels([f'{epochs[i-1]}-{epochs[i]}' for i in range(1, len(epochs))])

cbar2 = plt.colorbar(heatmap2, ax=ax3, orientation='vertical')
cbar2.set_label('Change in Efficiency Score', fontsize=10)

for i in range(len(yearly_trend)):
    for j in range(len(crews)):
        ax3.text(j, i, f'{yearly_trend[i, j]:+.1f}', ha='center', va='center', color='black', fontsize=8)

plt.tight_layout()
plt.show()