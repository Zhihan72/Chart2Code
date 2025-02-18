import matplotlib.pyplot as plt

devices = ['Tablets', 'Laptops', 'Gaming Consoles', 'Wearables', 'Smart TVs', 'Smartphones']
usage_percentage = [10, 8, 15, 35, 7, 25]

colors = ['#c0c0c0', '#ff6666', '#ffcc99', '#66b3ff', '#99ff99', '#ff9999']
explode = (0, 0, 0, 0.1, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    usage_percentage,
    labels=devices,
    colors=colors,
    autopct='%1.1f%%',
    startangle=45,
    explode=explode,
    wedgeprops=dict(edgecolor='black', linewidth=1, linestyle='--')
)

ax.axis('equal')
ax.set_title("Diverse Device Preferences:\nTechVille's Gadget Trends", fontsize=18, fontweight='light', pad=15)

plt.setp(autotexts, size=9, weight='light', color='white')
plt.setp(texts, size=11)

ax.legend(
    wedges, devices,
    title="Variety of Devices",
    loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9, frameon=False
)

plt.tight_layout()
plt.show()