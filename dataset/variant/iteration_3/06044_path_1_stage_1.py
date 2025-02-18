import matplotlib.pyplot as plt
import squarify

# Prepare data for the tree map
sizes = [7800, 4000, 3500000, 1200, 800000, 3000, 600, 200000, 15000, 1500, 500000, 100, 250, 100000, 1200]

# Create the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, alpha=0.8, pad=3)

# Show the tree map
plt.show()