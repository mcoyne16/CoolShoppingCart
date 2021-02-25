# shopping_cart.py
 
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#print(products)
import operator
def to_usd(my_price):
    return f"${my_price:,.2f}"

################################
#INPUTS CAPTURE
total_price = 0
selected_ids = []
while True:
    try:
        selected_id = input("Please input a product identifier: ")
        if selected_id.lower() == "done":
            break
        else:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]
            total_price = total_price + matching_product["price"]
            selected_ids.append(matching_product)
    except:
        print("Oops, please choose a valid ID from our product list")

################################
#OUTPUT DISPLAY

print("----------------------------------------")
print("MATT'S GROCERY STORE")
print("1 BAD ROUTE ROAD, GLENDIVE, MONTANA")
print("WWW.MYCOOLGROCERYSTORE.COM")
print("----------------------------------------")

date = datetime.date.today()
time = datetime.datetime.now()
print("CHECKOUT AT: ", date, time.strftime("%I:%M:%S %p"))
print("----------------------------------------")

print("SELECTED PRODUCTS:")
for matching_product in selected_ids:
    total_price = total_price + matching_product["price"]
    print("...", matching_product["name"], "(", str(to_usd(matching_product["price"])), ")")

print("----------------------------------------")
print("SUBTOTAL: ", str(to_usd(total_price)))
tax_rate = os.getenv("TAX_RATE", default="0.0875")
sales_tax = total_price * float(tax_rate)
print("TAX:       " + str(to_usd(sales_tax)))
final_price = total_price + sales_tax
print("TOTAL:     " + str(to_usd(final_price)))
print("----------------------------------------")
print("THANK YOU, PLEASE COME AGAIN!")
print("----------------------------------------")

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='mcoyne1699@gmail.com',
    to_emails='mcoyne1699@gmail.com',
    subject='Your Cool Shopping Cart Receipt',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send("TOTAL:     " + str(to_usd(final_price)))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
