
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

"""
LINE PLT
"""

# Read csv file 
vaccine = pd.read_csv('vaccination-data.csv')
print(vaccine)

# Plotting multiple lines graph
plt.figure(figsize=(8,8))
plt.plot(vaccine["TOTAL_VACCINATIONS_PER100"], label="total vaccinations")
plt.plot(vaccine["PERSONS_VACCINATED_1PLUS_DOSE_PER100"], label="1plus vaccinations")
plt.plot(vaccine["PERSONS_FULLY_VACCINATED_PER100"], label="fully vaccinations")
plt.legend()
plt.xlabel("Data")
plt.ylabel("Vaccinations")
plt.show()


"""
HISTOGRAM PLT
"""
# Read csv file
avocado = pd.read_csv('lineplt.csv')
print(avocado)

# Plotting 2 histograms with features
plt.figure(figsize=(8,8))
plt.hist(avocado["Small Bags"], label="Small Bags", alpha=0.8, bins=4)
plt.hist(avocado["Large Bags"], label="Large Bags", alpha=0.8 ,bins=4)
plt.legend()
plt.xlabel("Number of Bags")
plt.ylabel("Frequency")
plt.show()

"""
PIE PLT
"""

# Read csv file
book = pd.read_csv('bookings.csv')
print(book)

# Adding labels to pie graph
name = ["Summer", "Fall", "Winter", "Spring"]

# Plotting pie chart with values
plt.figure()
plt.pie(book["transactions"], labels=name, autopct='%1.1f%%') # 'autopct' is used for adding percentage to portions
plt.title("Total Number of Transactions in Every Season")
plt.show()
