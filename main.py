hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
# print("Average Haircut Price:", average_price)

new_prices = [price -  5 for price in prices]
# print('Old Prices:', prices)
# print('New Prices', new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  actual_sale = prices[i] * last_week[i]
  total_revenue += actual_sale

# print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
# print(average_daily_revenue)

# === Create list under 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)

# output:collection:condition





