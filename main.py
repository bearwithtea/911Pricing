import pandas as pd
import matplotlib.pyplot as plt

headers = ['Car', 'Price', 'Year Sold']

df = pd.read_csv('Cars and Bids - Pricing.csv', names=headers)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

df.set_index('Car', inplace=True)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df.plot(kind='line', title='Car Prices', color='blue', marker='o', fontsize=10, rot=90, legend=False)

plt.show()