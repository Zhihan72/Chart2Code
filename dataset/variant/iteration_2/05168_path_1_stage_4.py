import matplotlib.pyplot as plt

# Days of the week with randomized placement maintaining structure
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Temperature data for three cities with altered values while preserving dimensional integrity
new_york_temp = [58, 62, 55, 61, 63, 60, 65]
san_francisco_temp = [54, 56, 53, 57, 50, 52, 55]
miami_temp = [80, 81, 75, 78, 76, 77, 82]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature data with updated colors
ax.plot(days, new_york_temp, marker='o', linestyle='-', color='orange')
ax.plot(days, san_francisco_temp, marker='s', linestyle='--', color='purple')
ax.plot(days, miami_temp, marker='^', linestyle=':', color='teal')

# Remove axes borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Display the plot
plt.show()