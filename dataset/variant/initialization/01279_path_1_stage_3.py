import matplotlib.pyplot as plt

communication_methods = [
    'Email', 'IM', 'Vid Call', 'In-Person',
    'Collab Tool', 'Phone', 'Grp Vid Call', '1-on-1 Vid'
]

productivity_scores = [
    [78, 72, 79, 75, 87, 76, 83, 80, 80, 84, 85, 78, 83, 79, 81, 80, 82],  # Emails
    [93, 90, 86, 89, 89, 90, 87, 88, 91, 85, 91, 88, 87, 90, 90, 88, 92],  # Instant Messaging
    [73, 65, 68, 62, 66, 69, 67, 74, 69, 72, 70, 71, 70, 68, 69, 70, 67],  # Video Calls
    [80, 79, 82, 83, 78, 84, 82, 80, 85, 84, 82, 81, 83, 83, 85, 81, 84],  # In-Person Meetings
    [95, 94, 91, 93, 95, 92, 94, 96, 92, 90, 93, 94, 92, 94, 91, 93, 92],  # Collaborative Tools
    [79, 78, 78, 84, 80, 81, 83, 80, 82, 82, 85, 81, 81, 79, 82, 80, 85],  # Phone Calls
    [68, 70, 69, 66, 70, 73, 73, 72, 71, 66, 74, 65, 67, 70, 69, 68, 69],  # Group Video Calls
    [76, 68, 71, 71, 74, 72, 72, 75, 74, 72, 73, 76, 75, 69, 69, 70, 69]   # One-on-One Video Calls
]

plt.figure(figsize=(14, 10))
box = plt.boxplot(
    productivity_scores,
    patch_artist=True,
    labels=communication_methods,
    notch=True,
    vert=True,
    showmeans=True,
    meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black", "markersize": 8}
)

colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0', '#FFB6C1', '#ADD8E6', '#90EE90']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.xlabel('Methods', fontsize=14)
plt.ylabel('Productivity', fontsize=14)
plt.tight_layout()
plt.show()