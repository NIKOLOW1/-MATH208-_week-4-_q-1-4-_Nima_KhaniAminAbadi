{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import matplotlib.pyplot as plt\
\
# Function to calculate the mean of a list of numbers\
def calculate_mean(numbers):\
    return sum(numbers) / len(numbers)\
\
# Function to calculate the median of a list of numbers\
def calculate_median(numbers):\
    numbers.sort()\
    n = len(numbers)\
    if n % 2 == 0:\
        middle1 = numbers[n // 2]\
        middle2 = numbers[n // 2 - 1]\
        median = (middle1 + middle2) / 2\
    else:\
        median = numbers[n // 2]\
    return median\
\
# Function to calculate the standard deviation of a list of numbers\
def calculate_std_dev(numbers):\
    mean = calculate_mean(numbers)\
    squared_diff = [(x - mean) ** 2 for x in numbers]\
    variance = sum(squared_diff) / len(numbers)\
    std_dev = variance ** 0.5\
    return std_dev\
\
# Generate 500 random numbers with mean=10 and std_dev=0.5\
random_numbers = [random.gauss(10, 0.5) for _ in range(500)]\
\
# Calculate mean, median, and standard deviation\
mean = calculate_mean(random_numbers)\
median = calculate_median(random_numbers)\
std_dev = calculate_std_dev(random_numbers)\
\
# Print the results\
print("Mean:", mean)\
print("Median:", median)\
print("Standard Deviation:", std_dev)\
\
# Plot a histogram with 10 bins\
plt.hist(random_numbers, bins=10, edgecolor='k')\
plt.title("Histogram of Random Numbers (Gaussian)")\
plt.xlabel("Value")\
plt.ylabel("Frequency")\
plt.show()\
}