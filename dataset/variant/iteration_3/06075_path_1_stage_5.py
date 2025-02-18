import matplotlib.pyplot as plt

flavors = ['Choc', 'Van', 'Strawb', 'Mint Choc', 'Cookie D']
popularity = [25, 20, 15, 10, 10]

colors = ['#FFB6C1', '#FF9999', '#FFCC99', '#99FF99', '#66B3FF']  # Shuffled colors
explode = (0, 0.1, 0.1, 0, 0)  # Changed explode pattern

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=270,  # Changed to alter pie rotation
    colors=colors, 
    explode=explode,
    shadow=False,  # Removed shadow
    textprops=dict(color="darkblue"),  # Changed text color
    wedgeprops=dict(edgecolor='w', linestyle='--', linewidth=2)  # Changed border style
)

plt.setp(autotexts, size=12, fontstyle="italic")  # Changed text style

ax.set_title(
    "Ice Cream Preferences in Sweetvale", 
    fontsize=16, color='purple'  # Changed title styling
)
# Changed legend properties
ax.legend(
    wedges, flavors, title="Flavors", loc="upper right", frameon=True, framealpha=0.6
)

plt.tight_layout()

plt.show()