# Write your code here :-)
import codecademylib3
import pandas as pd

#funnel to describe process:
#user visits website, user adds to cart, user clicks checkout, user purchases

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])
#merge visits & cart
visits_carts = visits.merge(cart, how = 'left')
#how long is our new data frame? 2000
total_visits_carts = (len(visits_carts))
#how many rows are null? 1652
total_null_visits_carts = len(visits_carts[visits_carts.cart_time.isnull()])
#find percentage of no add cart
percent_users_noshirt = float(total_null_visits_carts / total_visits_carts)
#print(percent_users_noshirt)

#now find the abandoned cart percentage


cart_checkout = cart.merge(checkout, how = 'left')
#total null checkout times (no checkout)
total_null_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
#abandoned cart percentage, 25%
percent_abandoned_cart = float(total_null_cart_checkout / len(cart_checkout))
#print(percent_abandoned_cart)

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')


#the checkout--> purchase is the weakest funnel, consider optimizing checkout page

#calculate average time from initial visit to final purchase, add column (basically how long it takes to purchase)

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#print(all_data['time_to_purchase'])

#calculate average time to purchase

print(all_data['time_to_purchase'].mean())
#00:43:53 average funnel time to purchase
