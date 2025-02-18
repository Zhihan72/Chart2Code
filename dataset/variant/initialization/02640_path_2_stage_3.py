import matplotlib.pyplot as plt

categories = ["Tech Gadgets", "Apparel", "Home Goods", "Literature", "Wellness Products"]

# Manually altered sales data to reflect "random" changes while preserving dimensions
electronics_sales = [127, 120, 138, 122, 133, 135, 128, 132, 125, 130, 121, 140]
fashion_sales = [91, 87, 95, 88, 89, 90, 92, 94, 85, 86, 93, 90]
home_kitchen_sales = [154, 150, 162, 157, 148, 155, 148, 149, 155, 161, 158, 151]
books_sales = [67, 63, 62, 66, 70, 68, 64, 60, 69, 71, 61, 65]
health_beauty_sales = [119, 110, 115, 117, 112, 118, 122, 120, 114, 116, 113, 121]

data = [
    electronics_sales,
    fashion_sales,
    home_kitchen_sales,
    books_sales,
    health_beauty_sales
]

fig, ax = plt.subplots(figsize=(12, 6))

box = ax.boxplot(data, notch=True, patch_artist=True, vert=False,
                 boxprops=dict(facecolor="lightblue", color="blue"),
                 capprops=dict(color="blue"),
                 whiskerprops=dict(color="blue"),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'),
                 medianprops=dict(color="red"))

colors = ['#A2D9CE', '#F9E79F', '#F5B7B1', '#AED6F1', '#D2B4DE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title("Yearly Comparison of Sales\nin Miscellaneous Sectors: 2023", fontsize=14, fontweight='bold')
ax.set_xlabel('Units Sold (Thousands)', fontsize=12)
ax.set_yticks(range(1, len(categories) + 1))
ax.set_yticklabels(categories, fontsize=11)

ax.xaxis.grid(True, linestyle='--', which='both', alpha=0.7)

ax.legend([box["boxes"][i] for i in range(len(categories))], categories, loc='upper right', fontsize=9, title="Sections")

plt.tight_layout()
plt.show()