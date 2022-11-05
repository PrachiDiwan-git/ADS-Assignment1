
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

"""
LINE PLT
"""

# Read csv file 
data = pd.read_csv('vaccination-data.csv')
print(data)

# Plotting multiple lines graph
plt.figure(figsize=(8,8))
plt.plot(data["TOTAL_VACCINATIONS_PER100"], label="total Vaccinations")
plt.plot(data["PERSONS_VACCINATED_1PLUS_DOSE_PER100"], label="1Plus Vaccinations")
plt.plot(data["PERSONS_FULLY_VACCINATED_PER100"], label="Fully Vaccinations")
plt.legend()
plt.xlabel("Data")
plt.ylabel("Vaccinations")
plt.show()


"""
HISTOGRAM PLT
"""
# Read csv file
data2 = pd.read_csv('lineplt.csv')
print(data2)

# Plotting 2 histograms with features
plt.figure(figsize=(8,8))
plt.hist(data2["Small Bags"], label="Small Bags", alpha=0.8, bins=4)
plt.hist(data2["Large Bags"], label="Large Bags", alpha=0.8 ,bins=4)
plt.legend()
plt.xlabel("Number of Bags")
plt.ylabel("Frequency")
plt.show()

"""
PIE PLT
"""

# Read csv file
data3 = pd.read_csv('bookings.csv')
print(data3)

# Adding labels to pie graph
name = ["Summer", "Fall", "Winter", "Spring"]

# Plotting pie chart with values
plt.figure()
plt.pie(data3["transactions"], labels=name, autopct='%1.1f%%')
plt.title("Total Number of Transactions in Every Season")
plt.show()