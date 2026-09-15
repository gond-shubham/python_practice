import csv

try:
    with open("products.csv", 'r') as products:
        product = csv.reader(products)
        next(product)
        total_quantity_sold=0
        total_revenue=0
        highest_revenue_product= {"product":{"name":None,
                                     "revenue": None}}
        revenue_by_category={}

        for item in product:
          try:
              name, category, quantity, price=item
              quantity=int(quantity)
              price=int(price)

              total_quantity_sold+=quantity
              total_revenue+=quantity*price
              value=revenue_by_category.get(category, 0)
              revenue_by_category[category]=value+quantity*price


              if highest_revenue_product["product"]["revenue"] is None  or highest_revenue_product["product"]["revenue"]<quantity*price:
                      highest_revenue_product["product"]["revenue"]=quantity*price
                      highest_revenue_product["product"]["name"]=name
          except ValueError as e:
              print(f'value error {e} for the product {item}')
except FileNotFoundError:
        print("File does not exist")
        exit()
except OSError:
        print("Unable to open the file")
        exit()
except StopIteration:
        print("No data found in file")
        exit()


print(total_quantity_sold)
print(total_revenue)
print(highest_revenue_product)
print(revenue_by_category)






