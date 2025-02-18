import matplotlib.pyplot as plt

categories = [
    "Electronics", "Fashion", "Home & Kitchen", "Books", 
    "Health & Beauty", "Toys & Games", "Automotive"
]

electronics_sales = [120, 130, 125, 140, 135, 128, 127, 132, 138, 122, 121, 133]
fashion_sales = [85, 95, 90, 89, 92, 94, 87, 88, 91, 86, 93, 90]
home_kitchen_sales = [150, 160, 155, 148, 162, 157, 151, 149, 163, 154, 158, 161]
books_sales = [60, 65, 63, 70, 68, 66, 62, 67, 69, 64, 61, 71]
health_beauty_sales = [110, 115, 118, 112, 120, 119, 117, 116, 121, 114, 113, 122]
toys_games_sales = [70, 75, 73, 78, 76, 74, 72, 77, 79, 71, 69, 80]
automotive_sales = [95, 100, 98, 102, 101, 99, 97, 96, 103, 94, 93, 104]

data = [
    electronics_sales, fashion_sales, home_kitchen_sales, books_sales, 
    health_beauty_sales, toys_games_sales, automotive_sales
]

fig, ax = plt.subplots(figsize=(12, 6))

box = ax.boxplot(data, notch=False, patch_artist=True, vert=False,
                 boxprops=dict(facecolor="lightgray", color="green"),
                 capprops=dict(color="green"),
                 whiskerprops=dict(color="green"),
                 flierprops=dict(markerfacecolor='orange', marker='x', markersize=10, linestyle='none'),
                 medianprops=dict(color="purple"))

# New set of colors for the boxplots
new_colors = ['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#40E0D0', '#FF4500', '#7FFF00']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)

ax.set_yticks(range(1, len(categories) + 1))
ax.set_yticklabels([])

ax.xaxis.grid(True, linestyle='-', which='major', alpha=0.3)

plt.tight_layout()
plt.show()