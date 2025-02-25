import matplotlib.pyplot as plt

# Define trade routes with their respective trade volumes
trade_routes = [
    ("Sun City", "Moon Valley", 75), 
    ("Moon Valley", "Star Town", 65), 
    ("Star Town", "Comet Ridge", 50), 
    ("Comet Ridge", "Eclipse Bay", 40), 
    ("Eclipse Bay", "Meteor Plains", 55), 
    ("Meteor Plains", "Nebula Hill", 35), 
    ("Nebula Hill", "Galaxy Hamlet", 45), 
    ("Galaxy Hamlet", "Aurora Village", 30),
    ("Aurora Village", "Sun City", 60), 
    ("Sun City", "Meteor Plains", 50), 
    ("Moon Valley", "Eclipse Bay", 35), 
    ("Comet Ridge", "Nebula Hill", 50), 
    ("Star Town", "Aurora Village", 40)
]

# Extract trade volume information and sort them in descending order
trade_volumes = sorted(trade_routes, key=lambda x: x[2], reverse=True)

# Prepare data for plotting
routes_labels = [f"{u} → {v}" for u, v, w in trade_volumes]
volumes = [w for u, v, w in trade_volumes]

# Plotting the sorted bar chart with altered styles
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(routes_labels, volumes, color='lightgreen', edgecolor='darkgreen', linestyle='--')

# Altering marker type (in bar chart, use edge line style and color)
marker_style = dict(marker='o', markersize=8, color='red') 
for y, (label, vol) in enumerate(zip(routes_labels, volumes)):
    ax.plot(vol, y, **marker_style)

# Modify grid style
ax.grid(True, linestyle=':', linewidth=0.5, color='grey')

# Add a legend
ax.legend(['Trade Volume'], loc='lower right', frameon=False)

# Altering border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()