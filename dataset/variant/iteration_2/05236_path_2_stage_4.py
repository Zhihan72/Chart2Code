import matplotlib.pyplot as plt
import matplotlib.patches as patches

stages = [
    "Engagement",
    "Awareness Campaign",
    "Traffic Generation",
    "Convert to Customers",
    "Sales Pitch",
    "Lead Generation"
]

audience_counts = [16000, 50000, 30000, 2000, 4000, 8000]
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
markers = ['o', '^', 's', 'p', '*', 'x']
line_styles = ['-', '--', '-.', ':', '-', '--']
edge_colors = ['black', 'grey', 'blue', 'green', 'purple', 'orange']

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, max(audience_counts) + 5000)
ax.set_ylim(0, len(stages))

for i in range(len(stages) - 1):
    left = (max(audience_counts) - audience_counts[i])/2
    width_top = audience_counts[i]
    width_bottom = audience_counts[i + 1]
    height = 1
    line_style = line_styles[i]
    edge_color = edge_colors[i]

    trapezoid = patches.Polygon(
        [
            (left, i),
            (left + width_top, i),
            (left + (width_top + width_bottom)/2, i + height),
            (left + (width_top - width_bottom)/2, i + height)
        ],
        closed=True, color=new_colors[i], edgecolor=edge_color, linestyle=line_style
    )
    ax.add_patch(trapezoid)

left = (max(audience_counts) - audience_counts[-1])/2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), audience_counts[-1], 1, color=new_colors[-1], edgecolor=edge_colors[-1], linestyle=line_styles[-1]
)
ax.add_patch(rectangle)

ax.set_xticks([])
ax.set_yticks([])

ax.spines['top'].set_linestyle(':')
ax.spines['right'].set_visible(False)
ax.spines['left'].set_edgecolor('purple')
ax.spines['bottom'].set_linestyle('--')

plt.tight_layout()
plt.show()