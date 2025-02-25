import matplotlib.pyplot as plt

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