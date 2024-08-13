def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount if it's 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: %"))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price
    if discount_percentage >= 20:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
