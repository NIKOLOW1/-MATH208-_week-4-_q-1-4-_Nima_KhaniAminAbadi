import random
import matplotlib.pyplot as plt

# Function to calculate the mean 
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# calculate the median 
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        middle1 = numbers[n // 2]
        middle2 = numbers[n // 2 - 1]
        median = (middle1 + middle2) / 2
    else:
        median = numbers[n // 2]
    return median

# calculate the standard deviation 
def calculate_std_dev(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / len(numbers)
    std_dev = variance ** 0.5
    return std_dev

# Generate 500 random numbers with mean=10 and std_dev=0.5
random_numbers = [random.gauss(10, 0.5) for _ in range(500)]

# Calculate mean, median, and standard deviation
mean = calculate_mean(random_numbers)
median = calculate_median(random_numbers)
std_dev = calculate_std_dev(random_numbers)

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# Plot a histogram with 10 bins
plt.hist(random_numbers, bins=10, edgecolor='k')
plt.title("Histogram of Random Numbers (Gaussian)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
