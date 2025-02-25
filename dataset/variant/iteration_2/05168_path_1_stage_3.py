import matplotlib.pyplot as plt

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Temperature data for three cities
new_york_temp = [55, 60, 58, 62, 65, 63, 61]
san_francisco_temp = [50, 52, 54, 53, 55, 56, 57]
miami_temp = [75, 77, 76, 78, 80, 81, 82]

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