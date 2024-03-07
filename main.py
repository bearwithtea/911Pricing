import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('Cars and Bids - Pricing.csv')

data['Date Sold'] = pd.to_datetime(data['Date Sold'])

start_date = '2020-01-01'
end_date = '2022-12-31'
mask = (data['Date Sold'] > start_date) & (data['Date Sold'] <= end_date)
data = data.loc[mask]

data = data.sort_values('Price')

plt.figure(figsize=(10, 6))
plt.plot(data['Date Sold'], data['Price']) 
plt.title('930, 964, and 993 Prices') 
plt.xlabel('Date Sold') 
plt.ylabel('Price') 
plt.show() 