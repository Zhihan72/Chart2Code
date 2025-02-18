import matplotlib.pyplot as plt

# Funnel stages and user data (manually shuffled for randomness)
stages = ["Trial", "Subscription", "Awareness", "Retention", "Consideration"]
user_counts = [15000, 2500, 10000, 20000, 6000]  # Shuffled manually
average_ratings = [4.0, 4.8, 4.2, 3.5, 4.5]  # Shuffled manually

# Corresponding manually shuffled colors for the stages
colors = ['#1f77b4', '#9467bd', '#2ca02c', '#ff7f0e', '#d62728']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
plt.subplots_adjust(wspace=0.4)

# Horizontal Bar Chart for User Counts
ax1.barh(stages, user_counts, color=colors)
ax1.set_xlabel('Counts of Users', fontsize=12)
ax1.set_xlim(0, max(user_counts) + 2000)
for i, count in enumerate(user_counts):
    ax1.text(count + 500, i, f'{count} sessions', va='center', fontsize=10)

# Horizontal Bar Chart for Average Ratings
ax2.barh(stages, average_ratings, color=colors)
ax2.set_xlabel('Avg. Rating (max=5)', fontsize=12)
ax2.set_xlim(0, 5)
for i, rating in enumerate(average_ratings):
    ax2.text(rating + 0.1, i, f"{rating:.1f} stars", va='center', fontsize=10)

plt.suptitle("Modified Chart Representation", fontsize=16)
plt.show()