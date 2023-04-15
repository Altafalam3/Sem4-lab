import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random datapoints between 0 and 100
data = np.random.randint(0, 101, 1000)

# Define bin edges
bins = np.arange(0, 105, 5)

# Create histogram with 20 bins
plt.hist(data, bins=bins, edgecolor='black')

# Set x-axis label for each bin range
plt.xticks(bins)

# Set y-axis label for count of datapoints in each bin
plt.ylabel('Frequency')

# Set x-axis label for distribution
plt.xlabel('Distribution')

# Set title for the histogram
plt.title('Distribution of Randomly Generated Datapoints')

# Display the histogram
plt.show()