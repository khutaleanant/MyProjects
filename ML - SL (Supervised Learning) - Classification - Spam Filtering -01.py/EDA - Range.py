import matplotlib.pyplot as plt

# List of product prices
prices = [20, 45, 30, 55, 40,100,200]

# Create a box plot
plt.boxplot(prices)
plt.title('Price Distribution of Products')
plt.ylabel('Price ($)')
plt.show()
