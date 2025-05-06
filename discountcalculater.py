def discount_calculator(price, discount_percent):
 
    if discount_percent >= 20:
       discount_amount = price * (discount_percent / 100)
       final_price = price - discount_amount
    else:
       final_price = price
#getting input from user
    price = float(input("Enter the price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = discount_calculator(price, discount_percent)
    
    print(f"The final price after discount is: {final_price:.2f}")       
       