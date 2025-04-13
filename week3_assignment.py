# Discount Calculation
def calculate_discount(price, discount_percent):
    # Apply the discount if the discount percentage is 20% or higher
    if discount_percent >= 20:
        price = price - (price * discount_percent / 100)
    return price

# Prompt the user to enter the original price and discount percentage  
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: {final_price:.2f}")

# If no discount was applied, print the original price
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price:.2f}")