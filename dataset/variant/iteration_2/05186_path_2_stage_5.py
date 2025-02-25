import matplotlib.pyplot as plt

# Altered trade routes with changed town connections and volumes
trade_routes = [
    ("Eclipse Bay", "Sun City", 60), 
    ("Sun City", "Nebula Hill", 50), 
    ("Meteor Plains", "Star Town", 55), 
    ("Aurora Village", "Eclipse Bay", 35), 
    ("Comet Ridge", "Moon Valley", 50), 
    ("Galaxy Hamlet", "Meteor Plains", 40), 
    ("Moon Valley", "Galaxy Hamlet", 45), 
    ("Nebula Hill", "Comet Ridge", 30),
    ("Star Town", "Aurora Village", 65), 
    ("Sun City", "Moon Valley", 75), 
    ("Aurora Village", "Nebula Hill", 50), 
    ("Eclipse Bay", "Comet Ridge", 35), 
    ("Galaxy Hamlet", "Star Town", 40)
]

trade_volumes = sorted(trade_routes, key=lambda x: x[2], reverse=True)

routes_labels = [f"{u} → {v}" for u, v, w in trade_volumes]
volumes = [w for u, v, w in trade_volumes]

fig, ax = plt.subplots(figsize=(12, 8))
new_colors = ['deepskyblue', 'salmon', 'palegreen', 'orchid', 'gold', 'sandybrown', 'lightcoral', 'mediumorchid', 
              'lightslategray', 'lightseagreen', 'mediumpurple', 'khaki', 'lightpink']

ax.barh(routes_labels, volumes, color=new_colors, edgecolor='black', linestyle='--')

marker_style = dict(marker='o', markersize=8, color='navy')
for y, (label, vol) in enumerate(zip(routes_labels, volumes)):
    ax.plot(vol, y, **marker_style)

ax.grid(True, linestyle=':', linewidth=0.5, color='grey')

ax.legend(['Trade Volume'], loc='lower right', frameon=False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()