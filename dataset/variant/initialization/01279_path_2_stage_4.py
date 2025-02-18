import matplotlib.pyplot as plt

communication_methods = [
    'Emails', 'Instant Messaging', 'In-Person Meetings', 
    'Phone Calls', 'Group Video Calls', 'One-on-One Video Calls'
]

productivity_scores = [
    [72, 75, 78, 80, 83, 85, 87, 78, 80, 82, 79, 81, 84, 76, 80, 83, 79],
    [88, 89, 90, 92, 87, 91, 90, 93, 91, 87, 85, 88, 86, 89, 91, 90, 88],
    [77, 80, 82, 83, 81, 84, 85, 79, 82, 84, 78, 81, 80, 83, 85, 84, 82],
    [78, 80, 82, 81, 85, 83, 79, 80, 82, 81, 84, 85, 78, 80, 79, 81, 83],
    [65, 68, 70, 74, 69, 66, 73, 71, 69, 66, 70, 67, 72, 70, 68, 69, 73],
    [68, 71, 73, 76, 72, 70, 75, 74, 72, 69, 71, 69, 74, 72, 76, 75, 71]
]

plt.figure(figsize=(14, 10))
box = plt.boxplot(
    productivity_scores,
    patch_artist=True,
    labels=communication_methods,
    notch=False,
    vert=False,
    showmeans=True,
    meanprops={"marker": "s", "markerfacecolor": "purple", "markeredgecolor": "yellow", "markersize": 10}
)

colors = ['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#5F9EA0', '#D2691E']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title(
    'Communication Styles and Productivity:\nA Varied Approach Analysis', 
    fontsize=20, fontweight='bold', pad=20
)
plt.xlabel('Productivity Scores', fontsize=12)  # Change label position
plt.ylabel('Communication Methods', fontsize=12)  # Change label position

plt.grid(linestyle='-.', alpha=0.5)

handles = [plt.Line2D([0], [0], color=color, lw=5, linestyle='-') for color in colors]
plt.legend(handles, communication_methods, title='Methods', loc='upper right', fontsize=8)

plt.tight_layout()
plt.show()