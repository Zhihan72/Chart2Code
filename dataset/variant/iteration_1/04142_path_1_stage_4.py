import matplotlib.pyplot as plt

# Data for the donut chart
products = ['Smartwatches', 'Desktops', 'VR Headsets', 'Smart Lighting', 'Cyber Security']
revenue_percentages = [45, 25, 15, 10, 5]

colors = ['#4682B4', '#FFA07A', '#20B2AA', '#FFC0CB', '#9370DB']
explode = (0.1, 0.05, 0, 0.05, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    revenue_percentages,
    labels=products,
    autopct='%1.1f%%',
    startangle=120,
    colors=colors,
    explode=explode,
    shadow=False,
    wedgeprops=dict(width=0.4, edgecolor='g', linestyle='--')  # Modified wedge properties
)

plt.setp(autotexts, size=10, weight='bold', color='navy')  # Changed font settings
plt.setp(texts, size=11, style='italic')

plt.title('Income Distribution of InnovateCorp in 2023 across Sections', fontsize=16, fontweight='heavy')

# Randomly moved legend positioning and style
ax.legend(wedges, products, title="Product Categories", loc="upper left", fontsize=10, shadow=True)

ax.grid(True, linestyle=':', linewidth=0.5)  # Added a grid with a different style

ax.axis('equal')

plt.tight_layout()
plt.show()